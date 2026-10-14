"""Offline boundary tests for the isolated AWS MCP credential broker.

No real AWS credentials, network requests, IAM mutations or Docker daemon needed
for these unittest cases. CI executes them *inside* the pinned AWS runtime image.
"""
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import Mock, patch


def load(name, source):
    spec = importlib.util.spec_from_file_location(name, source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


process = load("role_credential_process", "/usr/local/bin/aws-mcp-credential-process.py")
broker = load("role_credential_broker", "/usr/local/bin/aws-mcp-credential-broker.py")

ROLE = "arn:aws:iam::123456789012:role/ChatGPTMcpReadOnlyRole"
ROLE_SESSION = "arn:aws:sts::123456789012:assumed-role/ChatGPTMcpReadOnlyRole/chatgpt-mcp-readonly"


def document(seconds=3600):
    return {
        "Version": 1,
        "AccessKeyId": "ASIATESTONLY",
        "SecretAccessKey": "unused-test-secret",
        "SessionToken": "unused-test-token",
        "Expiration": (dt.datetime.now(dt.timezone.utc) +
                       dt.timedelta(seconds=seconds)).isoformat(),
    }


class RoleCredentialProcessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name)
        self.directory.chmod(0o700)

    def stage(self, data=None, mode=0o600):
        p = self.directory / "credentials.json"
        p.write_text(json.dumps(data or document()), encoding="utf-8")
        p.chmod(mode)
        return p

    def test_only_role_json_validated_and_returned(self):
        self.stage()
        actual = process.read_role_credentials(self.directory)
        self.assertEqual(actual["Version"], 1)
        self.assertEqual(actual["AccessKeyId"], "ASIATESTONLY")

    def test_rejects_expired_and_nearly_expired(self):
        for lifetime in [-60, 20, 179]:
            with self.subTest(lifetime=lifetime):
                self.stage(document(lifetime))
                with self.assertRaises(ValueError):
                    process.read_role_credentials(self.directory)

    def test_rejects_public_file_and_directory(self):
        self.stage(mode=0o644)
        with self.assertRaises(ValueError):
            process.read_role_credentials(self.directory)
        self.stage()
        self.directory.chmod(0o755)
        with self.assertRaises(ValueError):
            process.read_role_credentials(self.directory)

    def test_rejects_symlink_and_malformed_payload(self):
        dest = self.stage()
        link = self.directory / "copy"
        dest.rename(link)
        dest.symlink_to(link)
        with self.assertRaises(ValueError):
            process.read_role_credentials(self.directory)
        dest.unlink()
        self.stage({"Version": 1, "AccessKeyId": "not-enough-fields"})
        with self.assertRaises(ValueError):
            process.read_role_credentials(self.directory)

    def test_broker_atomically_publishes_private_role_credentials(self):
        broker.atomic_publish(document(), self.directory)
        p = self.directory / "credentials.json"
        self.assertEqual(stat.S_IMODE(p.stat().st_mode), 0o600)
        self.assertEqual(process.read_role_credentials(self.directory)["Version"], 1)
        self.assertEqual(len(list(self.directory.iterdir())), 1)


class StsBrokerTests(unittest.TestCase):
    def response(self):
        cred = document()
        cred["Expiration"] = dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=1)
        return {"Credentials": cred, "AssumedRoleUser": {"Arn": ROLE_SESSION}}

    def test_role_identity_must_match(self):
        self.assertEqual(
            broker.make_role_document(self.response(), ROLE)["Version"], 1
        )
        with self.assertRaises(ValueError):
            broker.make_role_document(self.response(), "arn:aws:iam::000000000000:role/WrongRole")

    def test_assume_role_uses_session_policy_and_verifies_sts_identity(self):
        source = Mock()
        assumed = Mock()
        source.client.return_value.assume_role.return_value = self.response()
        assumed.client.return_value.get_caller_identity.return_value = {"Arn": ROLE_SESSION}
        with patch.object(broker.boto3, "Session", side_effect=[source, assumed]) as factory:
            result = broker.acquire(ROLE)
        self.assertEqual(result["AccessKeyId"], "ASIATESTONLY")
        factory.assert_any_call(profile_name="aws-mcp-readonly")
        source.client.return_value.assume_role.assert_called_once_with(
            RoleArn=ROLE,
            RoleSessionName="chatgpt-mcp-readonly",
            DurationSeconds=3600,
            PolicyArns=[{"arn": "arn:aws:iam::aws:policy/ReadOnlyAccess"}],
        )
        assumed.client.return_value.get_caller_identity.assert_called_once()
        self.assertNotIn("login_session", result)
        self.assertNotIn("role_arn", result)

    def test_rejects_impostor_temporary_identity(self):
        source = Mock()
        assumed = Mock()
        source.client.return_value.assume_role.return_value = self.response()
        assumed.client.return_value.get_caller_identity.return_value = {
            "Arn": "arn:aws:iam::123456789012:user/admin"
        }
        with patch.object(broker.boto3, "Session", side_effect=[source, assumed]):
            with self.assertRaises(ValueError):
                broker.acquire(ROLE)


if __name__ == "__main__":
    unittest.main()
