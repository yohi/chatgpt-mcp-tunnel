"""Offline tests for the optional manual STS session issuer (no AWS calls)."""
import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch

SOURCE=Path(__file__).resolve().parents[1] / 'scripts/aws-mcp-sts-quick.py'
spec=importlib.util.spec_from_file_location('quicksts',SOURCE)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class CredentialProcessTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.p=Path(self.tmp.name); self.p.chmod(0o700)
        self.document={
            'Version':1, 'AccessKeyId':'ASIA-test', 'SecretAccessKey':'test-key',
            'SessionToken':'test-token',
            'Expiration':(dt.datetime.now(dt.timezone.utc)+dt.timedelta(minutes=45)).isoformat(),
        }

    def test_atomic_publish_and_read(self):
        m.publish(self.document,self.p)
        self.assertEqual((self.p/'credentials.json').stat().st_mode & 0o777,0o600)
        self.assertEqual(m.read_credentials(self.p),self.document)

    def test_reject_expired_malformed_and_exposed(self):
        for minutes in (-1, 1):
            with self.subTest(minutes=minutes):
                d=dict(self.document); d['Expiration']=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(minutes=minutes)).isoformat()
                m.publish(d,self.p)
                with self.assertRaises(ValueError): m.read_credentials(self.p)
        m.publish({'Version':1,'AccessKeyId':'x'},self.p)
        with self.assertRaises(ValueError): m.read_credentials(self.p)
        m.publish(self.document,self.p)
        (self.p/'credentials.json').chmod(0o644)
        with self.assertRaises(ValueError): m.read_credentials(self.p)
        (self.p/'credentials.json').chmod(0o600)
        self.p.chmod(0o755)
        with self.assertRaises(ValueError): m.read_credentials(self.p)

    def test_reject_symlink(self):
        m.publish(self.document,self.p)
        target=self.p/'target';(self.p/'credentials.json').rename(target)
        (self.p/'credentials.json').symlink_to(target)
        with self.assertRaises(OSError): m.read_credentials(self.p)

    def test_source_profile_is_default(self):
        self.assertEqual(m.SOURCE_PROFILE, 'default')

    def test_assume_role_uses_managed_readonly_policy(self):
        sts=MagicMock()
        sts.get_caller_identity.return_value={'Account':'123456789012','Arn':'arn:aws:iam::123456789012:user/source'}
        role='arn:aws:iam::123456789012:role/ReadOnly'
        expiry=dt.datetime.now(dt.timezone.utc)+dt.timedelta(hours=1)
        sts.assume_role.return_value={'Credentials':{
            'AccessKeyId':'ASIA-mock','SecretAccessKey':'secret','SessionToken':'token','Expiration':expiry,
        },'AssumedRoleUser':{'Arn':'arn:aws:sts::123456789012:assumed-role/ReadOnly/aws-mcp-quick-readonly'}}
        source_session=MagicMock();source_session.client.return_value=sts
        probe_sts=MagicMock();probe_sts.get_caller_identity.return_value={'Arn':'arn:aws:sts::123456789012:assumed-role/ReadOnly/aws-mcp-quick-readonly'}
        probe_session=MagicMock();probe_session.client.return_value=probe_sts
        mock_boto3=MagicMock();mock_boto3.Session.side_effect=[source_session,probe_session]
        import sys
        with patch.dict(sys.modules,{'boto3':mock_boto3}):
            m.issue(role,self.p)
        self.assertEqual(sts.assume_role.call_args.kwargs['PolicyArns'],[{'arn':m.SESSION_POLICY}])
        self.assertEqual(m.read_credentials(self.p)['AccessKeyId'],'ASIA-mock')
        self.assertTrue((self.p/'credentials.json').exists())

    def test_multi_role_selection(self):
        multi_roles = (
            'arn:aws:iam::111111111111:role/AuditRole, '
            'arn:aws:iam::222222222222:role/AuditRole'
        )
        self.assertEqual(
            m.resolve_role_for_account(multi_roles, '222222222222'),
            'arn:aws:iam::222222222222:role/AuditRole'
        )
        with self.assertRaises(ValueError):
            m.resolve_role_for_account(multi_roles, '333333333333')


    def test_docker_login_startup_runner(self):
        script=(SOURCE.parent/'aws-mcp-quick-start.sh').read_text(encoding='utf-8')
        overlay=(SOURCE.parents[1]/'compose.aws.quick-sts.yaml').read_text(encoding='utf-8')
        self.assertIn('aws-auth login --remote --profile default',script)
        self.assertIn('aws-sso-init',script)
        self.assertIn('aws-quick-sts-issue',script)
        self.assertIn('\"${quick[@]}\" --profile aws-quick-sts-issue config --format json',script)
        self.assertIn('aws-quick-sts-clear',script)
        self.assertIn('aws-mcp-quick-sts:/run/aws-mcp-quick-sts:ro',overlay)
        self.assertIn('AWS_PROFILE: default',overlay)

if __name__=='__main__': unittest.main()
