import os
import subprocess
import sys
from pathlib import Path

import pytest
from dotenv import dotenv_values

REFERENCE_SCRIPTS = [
    ("binance_mcp_reference_implementation/binance_mcp.py", []),
    ("binance_mcp_reference_implementation/binance_mcp_w_prompt.py", []),
    ("binance_mcp_reference_implementation/binance_mcp_w_resource.py", []),
    ("binance_mcp/binance_mcp.py", []),
    ("langgraph/price_graph.py", []),
    (".github/run_price_graph_gemini.py", []),
    ("ref_openai_mcp/function_calling.py", ["openai"]),
    ("ref_openai_mcp/mcp_with_openai_agent.py", ["openai"]),
    ("ref_openai_mcp/mcp_with_responses_api.py", ["openai"]),
]

NOTEBOOKS = [
    "tool_calling.ipynb",
]

# Load .env only for missing env vars
if Path(".env").exists():
    env_config = dotenv_values(".env")
    for k, v in env_config.items():
        if k not in os.environ:
            os.environ[k] = v


def run_script(script_path):
    result = subprocess.run(
        [sys.executable, script_path], capture_output=True, text=True
    )
    print(f"\n--- Output of {script_path} ---\n{result.stdout}")
    if result.returncode != 0:
        print(f"--- Error output of {script_path} ---\n{result.stderr}")
    return result.returncode


def install_dependency_groups(groups):
    if not groups:
        return
    for g in groups:
        cmd = f"uv sync --group {g}"
        # Use bash to support process substitution
        result = subprocess.run(cmd, shell=True, executable="/bin/bash")
        if result.returncode != 0:
            raise RuntimeError(f"Failed to install dependency groups: {groups}")


@pytest.mark.parametrize("script_path,groups", REFERENCE_SCRIPTS)
def test_reference_script(script_path, groups):
    install_dependency_groups(groups)
    assert run_script(script_path) == 0


def run_notebook(notebook_path):
    result = subprocess.run(
        [sys.executable, "-m", "jupyter", "execute", notebook_path],
        capture_output=True,
        text=True,
    )
    print(f"\n--- Output of {notebook_path} ---\n{result.stdout}")
    if result.returncode != 0:
        print(f"--- Error output of {notebook_path} ---\n{result.stderr}")
    return result.returncode


@pytest.mark.parametrize("notebook_path", NOTEBOOKS)
def test_notebook(notebook_path):
    assert run_notebook(notebook_path) == 0


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
