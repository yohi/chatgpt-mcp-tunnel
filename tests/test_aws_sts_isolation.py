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
bootstrap = load("role_bootstrap", "/usr/local/bin/aws-mcp-bootstrap-role.py")

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


class RoleBootstrapTests(unittest.TestCase):
    def test_fixed_role_derived_from_iam_user_and_rejects_assumed_role(self):
        source, role, trust = bootstrap.describe_target({
            "Account": "123456789012",
            "Arn": "arn:aws:iam::123456789012:user/operator",
        })
        self.assertEqual(source, "arn:aws:iam::123456789012:user/operator")
        self.assertEqual(role, ROLE)
        self.assertEqual(trust["Statement"][0]["Principal"]["AWS"], source)
        with self.assertRaises(ValueError):
            bootstrap.describe_target({
                "Account": "123456789012",
                "Arn": ROLE_SESSION,
            })

    def test_default_role_resolution_uses_authenticated_account(self):
        session = Mock()
        session.client.return_value.get_caller_identity.return_value = {
            "Account": "123456789012",
            "Arn": "arn:aws:iam::123456789012:user/operator",
        }
        with patch.object(broker.boto3, "Session", return_value=session):
            self.assertEqual(broker.derive_role_arn(), ROLE)
        session.client.return_value.get_caller_identity.return_value = {
            "Account": "123456789012",
            "Arn": ROLE_SESSION,
        }
        with patch.object(broker.boto3, "Session", return_value=session):
            with self.assertRaises(ValueError):
                broker.derive_role_arn()

    def test_bootstrap_preview_does_not_create_iam_role(self):
        from botocore.exceptions import ClientError

        sts, iam = Mock(), Mock()
        sts.get_caller_identity.return_value = {
            "Account": "123456789012",
            "Arn": "arn:aws:iam::123456789012:user/operator",
        }
        iam.get_role.side_effect = ClientError(
            {"Error": {"Code": "NoSuchEntity", "Message": "absent"}},
            "GetRole",
        )
        source = Mock()
        source.client.side_effect = lambda name: {"sts": sts, "iam": iam}[name]
        self.assertEqual(bootstrap.bootstrap(source, apply=False), ROLE)
        iam.create_role.assert_not_called()
        iam.attach_role_policy.assert_not_called()

    def test_apply_only_creates_fixed_role_and_readonly_policy(self):
        from botocore.exceptions import ClientError

        identity = {
            "Account": "123456789012",
            "Arn": "arn:aws:iam::123456789012:user/operator",
        }
        _, _, trust = bootstrap.describe_target(identity)
        sts, iam = Mock(), Mock()
        sts.get_caller_identity.return_value = identity
        iam.get_role.side_effect = [
            ClientError(
                {"Error": {"Code": "NoSuchEntity", "Message": "absent"}},
                "GetRole",
            ),
            {"Role": {"Path": "/", "AssumeRolePolicyDocument": trust}},
        ]
        iam.list_attached_role_policies.return_value = {
            "AttachedPolicies": [{"PolicyArn": bootstrap.READ_ONLY_POLICY}]
        }
        iam.list_role_policies.return_value = {"PolicyNames": []}
        session = Mock()
        session.client.side_effect = lambda name: {"sts": sts, "iam": iam}[name]
        self.assertEqual(bootstrap.bootstrap(session, apply=True), ROLE)
        creation = iam.create_role.call_args.kwargs
        self.assertEqual(creation["RoleName"], "ChatGPTMcpReadOnlyRole")
        self.assertEqual(json.loads(creation["AssumeRolePolicyDocument"]), trust)
        self.assertEqual(creation["MaxSessionDuration"], 3600)
        iam.attach_role_policy.assert_called_once_with(
            RoleName="ChatGPTMcpReadOnlyRole",
            PolicyArn="arn:aws:iam::aws:policy/ReadOnlyAccess",
        )

    def test_existing_role_with_extra_permissions_is_refused(self):
        _, _, trust = bootstrap.describe_target({
            "Account": "123456789012",
            "Arn": "arn:aws:iam::123456789012:user/operator",
        })
        iam = Mock()
        iam.get_role.return_value = {
            "Role": {"Path": "/", "AssumeRolePolicyDocument": trust}
        }
        iam.list_attached_role_policies.return_value = {
            "AttachedPolicies": [
                {"PolicyArn": bootstrap.READ_ONLY_POLICY},
                {"PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"},
            ]
        }
        with self.assertRaises(ValueError):
            bootstrap.validate_existing_role(iam, bootstrap.ROLE_NAME, trust)
        iam.attach_role_policy.assert_not_called()


if __name__ == "__main__":
    unittest.main()
