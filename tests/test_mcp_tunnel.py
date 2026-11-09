"""Behavioral tests for the unified MCP tunnel command."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_SOURCE = ROOT / "scripts" / "mcp-tunnel"
SERVICES = {
    "--atlassian": "compose.atlassian.yaml",
    "--aws": "compose.aws.yaml",
    "--filesystem": "compose.filesystem.yaml",
}


class McpTunnelRunnerTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary_directory = tempfile.TemporaryDirectory(prefix="mcp-tunnel-test-")
        self.addCleanup(temporary_directory.cleanup)
        self.root = Path(temporary_directory.name) / "repo"
        self.scripts = self.root / "scripts"
        self.scripts.mkdir(parents=True)
        self.runner = self.scripts / "mcp-tunnel"
        if SCRIPT_SOURCE.is_file():
            shutil.copyfile(SCRIPT_SOURCE, self.runner)
        self.bin_directory = self.root / "bin"
        self.bin_directory.mkdir()
        self.call_log = self.root / "docker-calls.jsonl"
        self.cwd_log = self.root / "docker-cwds.log"
        self.run_cwd = self.root
        self._write_fake_docker()
        self._write_fixture_files()

    def _write_fake_docker(self) -> None:
        docker = self.bin_directory / "docker"
        docker.write_text(
            "#!/bin/sh\n"
            'printf "%s\\n" "$PWD" >> "$DOCKER_CALL_CWD_LOG"\n'
            "python3 -c 'import json,sys; f=open(sys.argv[1], "
            "\"a\"); f.write(json.dumps(sys.argv[2:])+\"\\n\"); f.close()' "
            '"$DOCKER_CALL_LOG" "$@"\n'
            'case "$*" in\n'
            '  *compose.aws.yaml*) [ "${FAIL_AWS:-0}" != 1 ] || exit 23 ;;\n'
            'esac\n',
            encoding="utf-8",
        )
        docker.chmod(0o700)

    def _write_fixture_files(self) -> None:
        for compose_file in SERVICES.values():
            (self.root / compose_file).write_text("services: {}\n", encoding="utf-8")
        (self.root / ".env").write_text("COMMON_VALUE=common\n", encoding="utf-8")
        for service in ("atlassian", "aws", "filesystem"):
            (self.root / f".env.{service}").write_text(
                f"SERVICE_VALUE={service}\n",
                encoding="utf-8",
            )

    def run_runner(self, *arguments: str, fail_aws: bool = False) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment["PATH"] = f"{self.bin_directory}{os.pathsep}{environment['PATH']}"
        environment["DOCKER_CALL_LOG"] = str(self.call_log)
        environment["DOCKER_CALL_CWD_LOG"] = str(self.cwd_log)
        environment["FAIL_AWS"] = "1" if fail_aws else "0"
        return subprocess.run(
            ["sh", str(self.runner), *arguments],
            cwd=self.run_cwd,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )

    def docker_calls(self) -> list[list[str]]:
        if not self.call_log.exists():
            return []
        return [json.loads(line) for line in self.call_log.read_text(encoding="utf-8").splitlines()]

    def docker_working_directories(self) -> list[str]:
        if not self.cwd_log.exists():
            return []
        return self.cwd_log.read_text(encoding="utf-8").splitlines()

    def test_default_operation_selects_only_atlassian(self) -> None:
        result = self.run_runner("--atlassian")

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.docker_calls()
        self.assertEqual(len(calls), 1)
        self.assertTrue(any(argument.endswith("compose.atlassian.yaml") for argument in calls[0]))
        self.assertIn("tunnel", calls[0])

    def test_aws_selection_maps_to_aws_compose_service(self) -> None:
        result = self.run_runner("--aws")

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = [call for call in self.docker_calls() if call[0] == "compose"]
        self.assertEqual(len(calls), 1)
        self.assertTrue(any(argument.endswith("compose.aws.yaml") for argument in calls[0]))
        self.assertIn("aws-tunnel", calls[0])

    def test_filesystem_selection_maps_to_filesystem_compose_service(self) -> None:
        result = self.run_runner("--filesystem")

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = [call for call in self.docker_calls() if call[0] == "compose"]
        self.assertEqual(len(calls), 1)
        self.assertTrue(any(argument.endswith("compose.filesystem.yaml") for argument in calls[0]))
        self.assertIn("filesystem-tunnel", calls[0])

    def test_all_selects_each_runtime_service(self) -> None:
        result = self.run_runner("--all")

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = [call for call in self.docker_calls() if call[0] == "compose"]
        self.assertEqual(len(calls), 3)
        self.assertEqual(
            [
                next(name for name in SERVICES.values() if any(arg.endswith(name) for arg in call))
                for call in calls
            ],
            list(SERVICES.values()),
        )

    def test_invalid_selection_fails_before_docker(self) -> None:
        for arguments in (
            ("unknown", "--atlassian"),
            ("--unknown",),
            ("--atlassian", "--atlassian"),
            ("--all", "--aws"),
            (),
        ):
            with self.subTest(arguments=arguments):
                result = self.run_runner(*arguments)

                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(self.docker_calls(), [])
                self.assertIn("usage", (result.stdout + result.stderr).lower())

    def test_help_prints_usage_without_running_docker(self) -> None:
        result = self.run_runner("--help")

        self.assertEqual(result.returncode, 0)
        self.assertIn("usage", result.stdout.lower())
        self.assertEqual(self.docker_calls(), [])

    def test_common_env_precedes_service_env_for_up(self) -> None:
        result = self.run_runner("--atlassian")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.docker_calls(),
            [[
                "compose",
                "--env-file", str(self.root / ".env"),
                "--env-file", str(self.root / ".env.atlassian"),
                "-f", str(self.root / "compose.atlassian.yaml"),
                "up", "-d", "tunnel",
            ]],
        )

    def test_atlassian_loads_existing_local_compose_override(self) -> None:
        (self.root / "compose.override.yaml").write_text("services: {}\n", encoding="utf-8")

        result = self.run_runner("--atlassian")

        self.assertEqual(result.returncode, 0, result.stderr)
        call = self.docker_calls()[0]
        self.assertEqual(
            [call[index + 1] for index, argument in enumerate(call) if argument == "-f"],
            [str(self.root / "compose.atlassian.yaml"), str(self.root / "compose.override.yaml")],
        )

    def test_lifecycle_operations_map_to_compose_commands(self) -> None:
        expected_commands = {
            "status": ["ps", "tunnel"],
            "logs": ["logs", "--tail=100", "tunnel"],
            "build": ["build", "tunnel"],
        }
        for operation, expected in expected_commands.items():
            with self.subTest(operation=operation):
                self.call_log.unlink(missing_ok=True)
                result = self.run_runner(operation, "--atlassian")

                self.assertEqual(result.returncode, 0, result.stderr)
                call = self.docker_calls()[0]
                self.assertEqual(call[-len(expected):], expected)

    def test_aws_and_filesystem_up_and_build_prepare_base_image_first(self) -> None:
        self.run_cwd = self.root / "scripts"
        selections = (("--aws", "compose.aws.yaml"), ("--filesystem", "compose.filesystem.yaml"))
        for selector, compose_file in selections:
            for operation in ("up", "build"):
                with self.subTest(selector=selector, operation=operation):
                    self.call_log.unlink(missing_ok=True)
                    self.cwd_log.unlink(missing_ok=True)
                    result = self.run_runner(operation, selector)

                    self.assertEqual(result.returncode, 0, result.stderr)
                    calls = self.docker_calls()
                    self.assertEqual(calls[0], ["build", "--tag", "chatgpt-mcp-tunnel:local", "."])
                    self.assertEqual(self.docker_working_directories()[0], str(self.root))
                    self.assertTrue(any(argument.endswith(compose_file) for argument in calls[1]))

    def test_legacy_atlassian_env_is_used_with_migration_warning(self) -> None:
        (self.root / ".env.atlassian").unlink()
        (self.root / ".env").write_text(
            "CONTROL_PLANE_TUNNEL_ID=tunnel-legacy\n"
            "CONTROL_PLANE_API_KEY=sk-legacy-secret\n",
            encoding="utf-8",
        )

        result = self.run_runner("--atlassian")

        self.assertEqual(result.returncode, 0, result.stderr)
        call = self.docker_calls()[0]
        self.assertEqual(call.count("--env-file"), 1)
        self.assertTrue(result.stderr.startswith("Warning:"))
        self.assertNotIn("sk-legacy-secret", result.stdout + result.stderr)

    def test_missing_common_env_fails_before_docker(self) -> None:
        (self.root / ".env").unlink()

        result = self.run_runner("--atlassian")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn(".env.example", result.stderr)
        self.assertEqual(self.docker_calls(), [])

    def test_missing_service_env_fails_before_docker(self) -> None:
        for selector, service in (("--aws", "aws"), ("--filesystem", "filesystem")):
            with self.subTest(service=service):
                self.call_log.unlink(missing_ok=True)
                (self.root / f".env.{service}").unlink()
                result = self.run_runner(selector)

                self.assertNotEqual(result.returncode, 0)
                self.assertIn(f".env.{service}.example", result.stderr)
                self.assertEqual(self.docker_calls(), [])

    def test_down_stops_and_removes_only_the_selected_container(self) -> None:
        result = self.run_runner("down", "--atlassian")

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.docker_calls()
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0][-2:], ["stop", "tunnel"])
        self.assertEqual(calls[1][-3:], ["rm", "--force", "tunnel"])
        self.assertTrue(all("compose.atlassian.yaml" in " ".join(call) for call in calls))
        self.assertFalse(any("down" in call or "volume" in call or "network" in call for call in calls))

    def test_multi_service_operation_continues_after_one_service_fails(self) -> None:
        result = self.run_runner("--aws", "--filesystem", fail_aws=True)

        self.assertNotEqual(result.returncode, 0)
        calls = self.docker_calls()
        self.assertTrue(any(any(arg.endswith("compose.aws.yaml") for arg in call) for call in calls))
        self.assertTrue(any(any(arg.endswith("compose.filesystem.yaml") for arg in call) for call in calls))

    def test_service_secret_is_not_printed(self) -> None:
        secret = "sk-test-secret-do-not-print"
        (self.root / ".env.aws").write_text(f"AWS_CONTROL_PLANE_API_KEY={secret}\n", encoding="utf-8")

        result = self.run_runner("--aws")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn(secret, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
