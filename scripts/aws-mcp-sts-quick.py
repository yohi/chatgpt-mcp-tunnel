#!/usr/bin/env python3
"""Opt-in single-shot STS issuer and role-only credential_process provider.

This is a temporary, manually renewed bridge. It never creates IAM roles.
The issuer alone can read the aws login cache; the MCP tunnel reads only
short-lived STS credentials from its separate private volume.
"""
import datetime as dt
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile

STORE = Path('/run/aws-mcp-quick-sts')
DOCUMENT = STORE / 'credentials.json'
SOURCE_PROFILE = 'default'
ROLE_ARN_RE = re.compile(r'^arn:aws:iam::([0-9]{12}):role/[A-Za-z0-9+=,.@_/-]+$')
SESSION_NAME = 'aws-mcp-quick-readonly'
SESSION_POLICY = 'arn:aws:iam::aws:policy/ReadOnlyAccess'
MIN_LIFETIME = 180


def check_store(directory=STORE):
    info = directory.lstat()
    if (not stat.S_ISDIR(info.st_mode) or info.st_uid != os.geteuid()
            or (info.st_mode & 0o077)):
        raise ValueError('private STS volume has unsafe owner or permissions')


def read_credentials(directory=STORE, now=None):
    check_store(directory)
    path = directory / 'credentials.json'
    fd = os.open(path, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
    try:
        info = os.fstat(fd)
        if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.geteuid()
                or (info.st_mode & 0o077)):
            raise ValueError('private STS document has unsafe owner or permissions')
        with os.fdopen(fd, 'r', encoding='utf-8') as handle:
            fd = -1
            item = json.load(handle)
    finally:
        if fd >= 0:
            os.close(fd)
    fields = ('AccessKeyId', 'SecretAccessKey', 'SessionToken', 'Expiration')
    if (not isinstance(item, dict) or set(item) != {'Version', *fields}
            or type(item.get('Version')) is not int or item['Version'] != 1
            or any(not isinstance(item.get(k), str) or not item[k] for k in fields)):
        raise ValueError('invalid STS document')
    expiry = dt.datetime.fromisoformat(item['Expiration'].replace('Z', '+00:00'))
    if expiry.tzinfo is None:
        raise ValueError('STS expiry has no timezone')
    now = now or dt.datetime.now(dt.timezone.utc)
    if (expiry - now).total_seconds() < MIN_LIFETIME:
        raise ValueError('STS credentials expired or too close to expiry')
    return item


def publish(item, directory=STORE):
    check_store(directory)
    fd, name = tempfile.mkstemp(prefix='.sts-', dir=directory)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            os.fchmod(handle.fileno(), 0o600)
            json.dump(item, handle, separators=(',', ':'))
            handle.write('\n')
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, directory / 'credentials.json')
        dfd = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def issue(role_arn, directory=STORE):
    match = ROLE_ARN_RE.fullmatch(role_arn or '')
    if not match:
        raise ValueError('set a valid same-account IAM role ARN')
    check_store(directory)
    # Remove the previous session before issuance: failure does not leave a
    # silently usable credential from a different role or earlier run.
    (directory / 'credentials.json').unlink(missing_ok=True)
    import boto3
    source = boto3.Session(profile_name=SOURCE_PROFILE)
    sts = source.client('sts')
    caller = sts.get_caller_identity()
    if caller.get('Account') != match.group(1) or caller.get('Arn', '').endswith(':root'):
        raise ValueError('login principal is root or role is in another account')
    result = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName=SESSION_NAME,
        DurationSeconds=3600,
        PolicyArns=[{'arn': SESSION_POLICY}],
    )
    creds = result['Credentials']
    expected_session_arn = (
        f'arn:aws:sts::{match.group(1)}:assumed-role/'
        f'{role_arn.rsplit("/", 1)[-1]}/{SESSION_NAME}'
    )
    if result['AssumedRoleUser']['Arn'] != expected_session_arn:
        raise ValueError('unexpected STS role-session identity')
    expires = creds['Expiration']
    if not isinstance(expires, dt.datetime) or expires.tzinfo is None:
        raise ValueError('missing STS expiry')
    item = {
        'Version': 1,
        'AccessKeyId': creds['AccessKeyId'],
        'SecretAccessKey': creds['SecretAccessKey'],
        'SessionToken': creds['SessionToken'],
        'Expiration': expires.astimezone(dt.timezone.utc).isoformat().replace('+00:00', 'Z'),
    }
    # Verify the actual newly issued principal before writing the file.
    probe = boto3.Session(
        aws_access_key_id=item['AccessKeyId'],
        aws_secret_access_key=item['SecretAccessKey'],
        aws_session_token=item['SessionToken'],
    )
    if probe.client('sts').get_caller_identity()['Arn'] != expected_session_arn:
        raise ValueError('STS credential identity mismatch')
    if (expires - dt.datetime.now(dt.timezone.utc)).total_seconds() < 600:
        raise ValueError('STS expiry too near for issuance')
    publish(item, directory)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('issue', 'read'):
        print('Usage: aws-mcp-sts-quick.py [issue|read]', file=sys.stderr)
        return 2
    try:
        if sys.argv[1] == 'issue':
            issue(os.environ.get('AWS_MCP_STS_ROLE_ARN', ''))
            print('STS session issued for read-only role (1 hour); renew manually.')
        else:
            json.dump(read_credentials(), sys.stdout, separators=(',', ':'))
            sys.stdout.write('\n')
        return 0
    except Exception:  # Never emit credentials, AWS responses, or source profile details.
        print('AWS MCP STS quick session unavailable; verify role, login, and volume.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
