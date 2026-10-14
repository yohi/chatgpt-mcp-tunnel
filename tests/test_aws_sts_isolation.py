"""Offline IAM lifecycle, STS role boundary and private credential tests."""
import datetime as dt
import importlib.util
import json
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import Mock, patch
from zoneinfo import ZoneInfo

from botocore.exceptions import ClientError


def load(name, source):
    spec = importlib.util.spec_from_file_location(name, source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


process = load("role_credential_process", "/usr/local/bin/aws-mcp-credential-process.py")
broker = load("role_credential_broker", "/usr/local/bin/aws-mcp-credential-broker.py")
bootstrap = load("role_bootstrap", "/usr/local/bin/aws-mcp-bootstrap-role.py")

ROLE_NAME = "ReadOnlyIAMRole_020261014142301"
ROLE = f"arn:aws:iam::123456789012:role/{ROLE_NAME}"
SOURCE = "arn:aws:iam::123456789012:user/operator"
ROLE_SESSION = f"arn:aws:sts::123456789012:assumed-role/{ROLE_NAME}/chatgpt-mcp-readonly"
IDENTITY = {"Account": "123456789012", "Arn": SOURCE}
RECORD = {
    "version": 1, "role_name": ROLE_NAME, "role_arn": ROLE,
    "role_id": "AROATESTONLY1234567890", "source_arn": SOURCE,
}


def document(seconds=3600):
    return {
        "Version": 1, "AccessKeyId": "ASIATESTONLY",
        "SecretAccessKey": "unused-test-secret", "SessionToken": "unused-test-token",
        "Expiration": (dt.datetime.now(dt.timezone.utc) +
                       dt.timedelta(seconds=seconds)).isoformat(),
    }


def aws_client_session():
    sts, iam = Mock(), Mock()
    sts.get_caller_identity.return_value = dict(IDENTITY)
    session = Mock()
    session.client.side_effect = lambda name: {"sts": sts, "iam": iam}[name]
    return session, sts, iam


class PrivateCredentialProcessTests(unittest.TestCase):
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

    def test_role_session_read(self):
        self.stage()
        self.assertEqual(process.read_role_credentials(self.directory)["AccessKeyId"],
                         "ASIATESTONLY")

    def test_rejects_expired_and_nearly_expired(self):
        for lifetime in (-60, 20, 179):
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
        p = self.stage()
        target = self.directory / "copy"
        p.rename(target)
        p.symlink_to(target)
        with self.assertRaises(ValueError):
            process.read_role_credentials(self.directory)
        p.unlink()
        self.stage({"Version": 1, "AccessKeyId": "incomplete"})
        with self.assertRaises(ValueError):
            process.read_role_credentials(self.directory)

    def test_atomic_publish(self):
        broker.atomic_publish(document(), self.directory)
        p = self.directory / "credentials.json"
        self.assertEqual(stat.S_IMODE(p.stat().st_mode), 0o600)
        self.assertEqual(len(list(self.directory.iterdir())), 1)


class StsRoleTests(unittest.TestCase):
    def response(self):
        credential = document()
        credential["Expiration"] = dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=1)
        return {"Credentials": credential, "AssumedRoleUser": {"Arn": ROLE_SESSION}}

    def test_role_identity_binding(self):
        self.assertEqual(broker.make_role_document(self.response(), ROLE)["Version"], 1)
        with self.assertRaises(ValueError):
            broker.make_role_document(self.response(),
                "arn:aws:iam::000000000000:role/OtherRole")

    def test_broker_includes_readonly_session_policy(self):
        source, assumed = Mock(), Mock()
        source.client.return_value.assume_role.return_value = self.response()
        assumed.client.return_value.get_caller_identity.return_value = {"Arn": ROLE_SESSION}
        with patch.object(broker.boto3, "Session", side_effect=[source, assumed]):
            self.assertEqual(broker.acquire(ROLE)["AccessKeyId"], "ASIATESTONLY")
        source.client.return_value.assume_role.assert_called_once_with(
            RoleArn=ROLE, RoleSessionName="chatgpt-mcp-readonly",
            DurationSeconds=3600,
            PolicyArns=[{"arn": "arn:aws:iam::aws:policy/ReadOnlyAccess"}],
        )

    def test_broker_refuses_wrong_sts_identity(self):
        source, assumed = Mock(), Mock()
        source.client.return_value.assume_role.return_value = self.response()
        assumed.client.return_value.get_caller_identity.return_value = {"Arn": SOURCE}
        with patch.object(broker.boto3, "Session", side_effect=[source, assumed]):
            with self.assertRaises(ValueError):
                broker.acquire(ROLE)

    def test_broker_reads_only_bound_managed_role_record(self):
        with tempfile.TemporaryDirectory() as d:
            home = Path(d)
            home.chmod(0o700)
            record_file = home / "role.json"
            record_file.write_text(json.dumps(RECORD))
            record_file.chmod(0o600)
            session = Mock()
            session.client.return_value.get_caller_identity.return_value = dict(IDENTITY)
            with patch.object(broker, "ROLE_STATE", record_file), patch.object(
                broker.boto3, "Session", return_value=session
            ):
                self.assertEqual(broker.derive_role_arn(), ROLE)
                session.client.return_value.get_caller_identity.return_value = {
                    "Account": "123456789012",
                    "Arn": "arn:aws:iam::123456789012:user/not-operator",
                }
                with self.assertRaises(ValueError):
                    broker.derive_role_arn()


class TimestampRoleLifecycleTests(unittest.TestCase):
    def test_exact_five_digit_year_mask_and_tokyo_clock(self):
        now = dt.datetime(2026, 10, 14, 14, 23, 1, tzinfo=ZoneInfo("Asia/Tokyo"))
        self.assertEqual(bootstrap.role_name_at(now), ROLE_NAME)
        self.assertTrue(bootstrap.ROLE_NAME_RE.fullmatch(bootstrap.role_name_at(now)))

    def test_role_owns_just_one_user_and_is_tagged(self):
        user, arn, trust, tags = bootstrap.describe_target(IDENTITY, ROLE_NAME)
        self.assertEqual(user, SOURCE)
        self.assertEqual(arn, ROLE)
        self.assertEqual(trust["Statement"][0]["Principal"]["AWS"], SOURCE)
        self.assertEqual({x["Key"]: x["Value"] for x in tags}, {
            "ManagedBy": "chatgpt-mcp-tunnel-temporary",
            "SourcePrincipal": SOURCE,
        })
        with self.assertRaises(ValueError):
            bootstrap.describe_target(
                {"Account": "123456789012", "Arn": ROLE_SESSION}, ROLE_NAME
            )

    def test_role_state_private_and_owner_bound(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            folder.chmod(0o700)
            state_file = folder / "role.json"
            bootstrap.save_state(RECORD, state_file)
            self.assertEqual(bootstrap.read_state(state_file), RECORD)
            self.assertEqual(stat.S_IMODE(state_file.stat().st_mode), 0o600)
            with self.assertRaises(ValueError):
                bootstrap.save_state(RECORD, state_file)
            state_file.chmod(0o644)
            with self.assertRaises(ValueError):
                bootstrap.read_state(state_file)

    def test_preview_does_not_mutate_iam(self):
        session, sts, iam = aws_client_session()
        with patch.object(bootstrap, "read_state", return_value=None), patch.object(
            bootstrap, "role_name_at", return_value=ROLE_NAME
        ):
            self.assertEqual(bootstrap.lifecycle(session, apply=False), ROLE)
        iam.create_role.assert_not_called()
        iam.attach_role_policy.assert_not_called()
        iam.delete_role.assert_not_called()

    def test_apply_only_creates_tagged_readonly_role(self):
        session, sts, iam = aws_client_session()
        iam.get_role.side_effect = ClientError(
            {"Error": {"Code": "NoSuchEntity", "Message": "not found"}}, "GetRole"
        )
        iam.create_role.return_value = {"Role": {"RoleId": RECORD["role_id"]}}
        with patch.object(bootstrap, "read_state", return_value=None), patch.object(
            bootstrap, "role_name_at", return_value=ROLE_NAME
        ), patch.object(bootstrap, "save_state") as save, patch.object(
            bootstrap, "validate_owned_role", return_value=[bootstrap.READ_ONLY_POLICY]
        ):
            self.assertEqual(bootstrap.lifecycle(session, apply=True), ROLE)
        create = iam.create_role.call_args.kwargs
        self.assertEqual(create["RoleName"], ROLE_NAME)
        self.assertEqual(create["Tags"], bootstrap.describe_target(
            IDENTITY, ROLE_NAME
        )[3])
        self.assertEqual(create["MaxSessionDuration"], 3600)
        self.assertEqual(json.loads(create["AssumeRolePolicyDocument"])[
            "Statement"][0]["Principal"]["AWS"], SOURCE)
        save.assert_called_once_with(RECORD)
        iam.attach_role_policy.assert_called_once_with(
            RoleName=ROLE_NAME, PolicyArn=bootstrap.READ_ONLY_POLICY
        )
        iam.delete_role.assert_not_called()

    def test_rejects_preexisting_role_name_collision(self):
        session, sts, iam = aws_client_session()
        iam.get_role.return_value = {"Role": {"RoleId": "AROADifferent"}}
        with patch.object(bootstrap, "read_state", return_value=None), patch.object(
            bootstrap, "role_name_at", return_value=ROLE_NAME
        ):
            with self.assertRaises(ValueError):
                bootstrap.lifecycle(session, apply=True)
        iam.create_role.assert_not_called()

    def test_validate_roleid_and_no_extra_permissions(self):
        session, sts, iam = aws_client_session()
        _, _, trust, tags = bootstrap.describe_target(IDENTITY, ROLE_NAME)
        iam.get_role.return_value = {
            "Role": {
                "Arn": ROLE, "RoleId": RECORD["role_id"], "Path": "/",
                "AssumeRolePolicyDocument": trust,
            }
        }
        def pages(name):
            results = {
                "list_role_tags": [{"Tags": tags}],
                "list_attached_role_policies": [{
                    "AttachedPolicies": [{"PolicyArn": bootstrap.READ_ONLY_POLICY}]
                }],
                "list_role_policies": [{"PolicyNames": []}],
                "list_instance_profiles_for_role": [{"InstanceProfiles": []}],
            }
            paginator = Mock()
            paginator.paginate.return_value = results[name]
            return paginator
        iam.get_paginator.side_effect = pages
        self.assertEqual(bootstrap.validate_owned_role(
            iam, RECORD, trust, tags, cleanup=True
        ), [bootstrap.READ_ONLY_POLICY])
        iam.get_role.return_value["Role"]["RoleId"] = "AROANotOurRole"
        with self.assertRaises(ValueError):
            bootstrap.validate_owned_role(iam, RECORD, trust, tags, cleanup=True)

    def test_cleanup_requires_both_services_stopped(self):
        session, sts, iam = aws_client_session()
        with patch.object(bootstrap, "read_state", return_value=RECORD):
            with self.assertRaises(ValueError):
                bootstrap.lifecycle(session, cleanup=True)
        iam.detach_role_policy.assert_not_called()
        iam.delete_role.assert_not_called()

    def test_cleanup_purges_cached_role_session_and_deletes_only_owned_role(self):
        session, sts, iam = aws_client_session()
        with patch.object(bootstrap, "read_state", return_value=RECORD), patch.object(
            bootstrap, "validate_owned_role", return_value=[bootstrap.READ_ONLY_POLICY]
        ), patch.object(bootstrap, "clear_cached_credentials") as clear, patch.object(
            bootstrap.STATE, "unlink"
        ) as unlink:
            self.assertIsNone(bootstrap.lifecycle(
                session, cleanup=True, confirmed_stopped=True
            ))
        clear.assert_called_once()
        iam.detach_role_policy.assert_called_once_with(
            RoleName=ROLE_NAME, PolicyArn=bootstrap.READ_ONLY_POLICY
        )
        iam.delete_role.assert_called_once_with(RoleName=ROLE_NAME)
        unlink.assert_called_once()

    def test_cleanup_different_user_fails_closed(self):
        session, sts, iam = aws_client_session()
        sts.get_caller_identity.return_value["Arn"] = (
            "arn:aws:iam::123456789012:user/not-the-owner"
        )
        with patch.object(bootstrap, "read_state", return_value=RECORD):
            with self.assertRaises(ValueError):
                bootstrap.lifecycle(session, cleanup=True, confirmed_stopped=True)
        iam.delete_role.assert_not_called()


if __name__ == "__main__":
    unittest.main()
