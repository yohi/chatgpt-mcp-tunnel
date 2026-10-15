"""Synthetic-only tests. Run in a network namespace with an empty HOME."""
import ast
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from experiments.aws_mcp_broker_v11_offline import validation as subject


class JsonInputTests(unittest.TestCase):
    REQUIRED = {"id": str, "version": int}

    def decode(self, data, **kwargs):
        return subject.decode_json(data, required_types=self.REQUIRED, **kwargs)

    def test_minimal_json_is_structural_only(self):
        result, item = self.decode(b'{"id":"synthetic","version":1}')
        self.assertEqual(result.status, "STRUCTURALLY_VALID")
        self.assertEqual(item, {"id": "synthetic", "version": 1})
        self.assertFalse(hasattr(result, "allow"))

    def test_duplicate_keys_any_depth_rejected(self):
        for data in (b'{"id":"a","id":"b","version":1}',
                     b'{"id":"a","version":1,"extra":{"x":1,"x":2}}'):
            with self.subTest(data=data):
                result, item = self.decode(data, optional_types={"extra": dict})
                self.assertEqual(result.status, "REJECTED")
                self.assertIsNone(item)

    def test_input_size_boundary(self):
        for data in (b"", b"123456789"):
            result, item = self.decode(data, max_bytes=8)
            self.assertEqual(result.status, "REJECTED")
            self.assertIsNone(item)
        result, _ = self.decode(b'{"id":"a","version":1}', max_bytes=22)
        self.assertEqual(result.status, "STRUCTURALLY_VALID")

    def test_malformed_utf8_and_json_and_nonfinite(self):
        for data in (b'\xff', b'\xef\xbb\xbf{}', b'{', b'{"id":NaN,"version":1}',
                     b'{"id":"a","version":Infinity}', b'[]', b'"string"'):
            with self.subTest(data=data):
                self.assertEqual(self.decode(data)[0].status, "REJECTED")

    def test_nested_nonfinite_and_unpaired_surrogates(self):
        cases = (b'{"id":"a","version":1,"extra":{"n":1e999}}',
                 b'{"id":"\\ud800","version":1}',
                 b'{"id":"a","version":1,"extra":{"\\udfff":1}}')
        for data in cases:
            with self.subTest(data=data):
                self.assertEqual(self.decode(data, optional_types={"extra": dict})[0].status,
                                 "REJECTED")

    def test_unknown_missing_and_type_confusion(self):
        for data in (b'{"id":"a"}', b'{"id":"a","version":1,"extra":true}',
                     b'{"id":"a","version":true}', b'{"id":null,"version":1}',
                     b'{"id":42,"version":1}'):
            with self.subTest(data=data):
                self.assertEqual(self.decode(data)[0].status, "REJECTED")
        self.assertEqual(self.decode(b'{"id":"a","version":1,"flag":false}',
                                     optional_types={"flag": bool})[0].status, "STRUCTURALLY_VALID")

    def test_invalid_schema_and_optional_overlap_rejected(self):
        for kwargs in ({"required_types": {"id": [str]}},
                       {"required_types": {"id": str}, "optional_types": {"id": str}},
                       {"required_types": {1: str}},
                       {"required_types": {"id": str}, "optional_types": {"x": object}}):
            result, _ = subject.decode_json(b'{"id":"a"}', **kwargs)
            self.assertEqual(result.status, "REJECTED")

    def test_nonbytes_and_invalid_schema_rejected_without_echo(self):
        self.assertEqual(self.decode("not bytes")[0].status, "REJECTED")
        self.assertEqual(self.decode(b'{}', max_bytes=True)[0].status, "REJECTED")


class DigestTests(unittest.TestCase):
    def test_digest_exact_bytes_and_lowercase_hex(self):
        raw = b'synthetic\x00bytes'
        digest = hashlib.sha256(raw).hexdigest()
        self.assertEqual(subject.check_sha256(raw, digest).status, "STRUCTURALLY_VALID")
        self.assertEqual(subject.check_sha256(raw, digest.upper()).status, "REJECTED")
        self.assertEqual(subject.check_sha256(raw + b'!', digest).status, "REJECTED")

    def test_invalid_and_missing_digests(self):
        for value in (None, "PENDING", "f" * 63, "g" * 64, b"a" * 64, "f" * 65):
            with self.subTest(value=value):
                self.assertEqual(subject.check_sha256(b'abc', value).status, "REJECTED")
        self.assertEqual(subject.check_sha256(None, "a" * 64).status, "REJECTED")


class BoundaryTests(unittest.TestCase):
    def test_pending_unsigned_and_synthetic_never_authorize(self):
        for proposed in (None, {}, {"status": "PENDING"},
                         {"status": "APPROVED"}, {"status": "VERIFIED", "signature": "synthetic"}):
            with self.subTest(proposed=proposed):
                result = subject.boundary_status(subject.ValidationResult("STRUCTURALLY_VALID", "OK"), proposed)
                self.assertEqual(result.status, "NOT_VERIFIED")
                self.assertFalse(hasattr(result, "allow"))

    def test_rejection_and_exceptions_cannot_be_allow(self):
        self.assertEqual(subject.boundary_status(subject.ValidationResult("REJECTED", "INVALID")).status,
                         "REJECTED")
        self.assertEqual(subject.boundary_status(None).status, "NOT_VERIFIED")
        result, _ = subject.decode_json(b'{"id":"FAKE_SECRET_DO_NOT_LEAK"}', required_types={"id": str}, max_bytes=3)
        self.assertNotIn("FAKE_SECRET", repr(result))

    def test_clock_injection_validates_aware_datetime_without_authority(self):
        clock = lambda: dt.datetime(2026, 10, 15, tzinfo=dt.timezone.utc)
        self.assertEqual(subject.inspect_clock(clock).status, "STRUCTURALLY_VALID")
        self.assertEqual(subject.inspect_clock(lambda: dt.datetime(2026, 10, 15)).status, "REJECTED")
        self.assertEqual(subject.inspect_clock(lambda: "wrong").status, "REJECTED")
        self.assertEqual(subject.inspect_clock(None).status, "REJECTED")
        class BrokenTimezone(dt.tzinfo):
            def utcoffset(self, _):
                return None
        self.assertEqual(subject.inspect_clock(lambda: dt.datetime(2026, 1, 1, tzinfo=BrokenTimezone())).status,
                         "REJECTED")
        def bad_clock():
            raise RuntimeError("FAKE_SECRET_DO_NOT_LEAK")
        status = subject.inspect_clock(bad_clock)
        self.assertEqual(status.status, "NOT_VERIFIED")
        self.assertNotIn("FAKE_SECRET", repr(status))

    def test_prohibited_modules_and_operations_absent_from_source(self):
        path = ROOT / 'experiments' / 'aws_mcp_broker_v11_offline' / 'validation.py'
        tree = ast.parse(path.read_text(encoding='utf-8'))
        forbidden_modules = {'boto3', 'botocore', 'socket', 'subprocess', 'requests', 'urllib',
                             'os', 'pathlib', 'awscli', 'http', 'logging'}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                self.assertTrue(all(a.name.split('.')[0] not in forbidden_modules for a in node.names))
            if isinstance(node, ast.ImportFrom) and node.module:
                self.assertNotIn(node.module.split('.')[0], forbidden_modules)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, {'open', 'exec', 'eval', '__import__'})


if __name__ == '__main__':
    unittest.main()
