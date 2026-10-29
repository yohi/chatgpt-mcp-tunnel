import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class FilesystemComposeTest(unittest.TestCase):
    def test_mount_is_read_only_and_tunnel_configuration_is_separate(self):
        with tempfile.TemporaryDirectory() as directory:
            env_file = Path(directory) / '.env.filesystem'
            env_file.write_text(
                'FILESYSTEM_CONTROL_PLANE_TUNNEL_ID=tunnel_filesystem_test\n'
                'FILESYSTEM_CONTROL_PLANE_API_KEY=sk-test\n'
                f'FILESYSTEM_HOST_PATH={directory}\n',
                encoding='utf-8',
            )
            result = subprocess.run(
                [
                    'docker', 'compose', '-f', 'compose.filesystem.yaml',
                    '--env-file', str(env_file), 'config', '--format', 'json',
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                env={**os.environ, 'COMPOSE_PROJECT_NAME': 'filesystem-test'},
            )

        config = json.loads(result.stdout)
        service = config['services']['filesystem-tunnel']
        self.assertEqual(
            service['environment']['CONTROL_PLANE_TUNNEL_ID'],
            'tunnel_filesystem_test',
        )
        self.assertIn('mcp-server-filesystem /projects', service['environment']['MCP_COMMAND'])
        self.assertTrue(any(
            mount['target'] == '/projects'
            and mount['read_only']
            and mount['source'] == directory
            for mount in service['volumes']
        ))
        self.assertNotIn('ports', service)

    def test_ci_validates_and_smoke_tests_filesystem_image(self):
        workflow = (ROOT / '.github/workflows/docker-build.yml').read_text(encoding='utf-8')
        self.assertIn(
            'docker compose --env-file .env.filesystem.example -f compose.filesystem.yaml config --quiet',
            workflow,
        )
        self.assertIn(
            'docker build -f Dockerfile.filesystem --tag chatgpt-filesystem-mcp-tunnel:ci .',
            workflow,
        )
        self.assertIn('docker pull node:24-bookworm-slim', workflow)
        self.assertIn('command -v mcp-server-filesystem', workflow)


if __name__ == '__main__':
    unittest.main()
