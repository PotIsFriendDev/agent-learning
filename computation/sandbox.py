import os
import subprocess
from typing import List

SANDBOX_ROOT = r"D:\claude-agent-learning\sandbox\workspace"

def _safe_path(path: str) -> str:
    """
    Resolves the path and ensures it is confined to the SANDBOX_ROOT.
    Raises PermissionError if the path escapes the root.
    """
    # Ensure the root exists
    if not os.path.exists(SANDBOX_ROOT):
        os.makedirs(SANDBOX_ROOT, exist_ok=True)

    # Resolve the absolute path
    abs_path = os.path.abspath(os.path.join(SANDBOX_ROOT, path))

    # Verify that the common path is the SANDBOX_ROOT
    if os.path.commonpath([abs_path, SANDBOX_ROOT]) != SANDBOX_ROOT:
        raise PermissionError(f"Access denied: Path {path} is outside the sandbox root.")

    return abs_path

def read_file(path: str) -> str:
    """Reads the content of a file within the sandbox."""
    safe_p = _safe_path(path)
    if not os.path.isfile(safe_p):
        raise FileNotFoundError(f"File not found: {path}")

    with open(safe_p, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    """Writes content to a file within the sandbox."""
    safe_p = _safe_path(path)

    # Ensure parent directory exists
    os.makedirs(os.path.dirname(safe_p), exist_ok=True)

    with open(safe_p, 'w', encoding='utf-8') as f:
        f.write(content)

    return f"Successfully wrote to {path}"

def list_files(path: str = ".") -> List[str]:
    """Lists entries in a directory within the sandbox."""
    safe_p = _safe_path(path)
    if not os.path.isdir(safe_p):
        raise NotADirectoryError(f"Not a directory: {path}")

    return os.listdir(safe_p)

def execute_script(path: str) -> str:
    """
    Executes a script (e.g. Python) within the sandbox.
    For simplicity, we assume Python scripts.
    """
    safe_p = _safe_path(path)
    if not os.path.isfile(safe_p):
        raise FileNotFoundError(f"Script not found: {path}")

    try:
        # Use subprocess.run with shell=False to avoid shell injection
        # Set cwd to SANDBOX_ROOT so the script itself executes within the sandbox
        result = subprocess.run(
            ["python", safe_p],
            cwd=SANDBOX_ROOT,
            capture_output=True,
            text=True,
            timeout=30
        )

        output = result.stdout
        if result.stderr:
            output += f"\nError: {result.stderr}"

        return output if output else "Script executed successfully with no output."

    except subprocess.TimeoutExpired:
        return "Error: Script execution timed out after 30 seconds."
    except Exception as e:
        return f"Error during execution: {str(e)}"
