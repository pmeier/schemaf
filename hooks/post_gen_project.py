import subprocess
import sys
import warnings
from os import path
from platform import system as _system
from typing import Optional


def run_cmd(executable: str, *args: str) -> None:
    cmd = " ".join((executable, *args))
    print(f"Running '{cmd}'")
    output = subprocess.check_output(cmd, shell=True)
    if output:
        print(output.decode("utf-8").strip())


def run_python_cmd(
    *args: str, executable: str = sys.executable, module: bool = False
) -> None:
    if module:
        args = ("-m", *args)
    run_cmd(executable, *args)


def run_pip_cmd(*args: str, python_executable: str = sys.executable) -> None:
    run_python_cmd("pip", *args, executable=python_executable, module=True)


def run_git_cmd(*args: str, path: Optional[str] = None) -> None:
    if path is not None:
        args = ("-C", path, *args)
    run_cmd("git", *args)


def initialize_git(
    project_root: str,
    user_name: str = "{{cookiecutter.author}}",
    user_email: str = "{{cookiecutter.author_email}}",
    initial_commit_msg: str = "Initial commit",
    url: str = "{{cookiecutter.url}}",
) -> None:
    run_git_cmd("init", project_root)
    run_git_cmd("config", "user.name", f'"{user_name}"', path=project_root)
    run_git_cmd("config", "user.email", f'"{user_email}"', path=project_root)
    run_git_cmd("add", ".", path=project_root)
    run_git_cmd("commit", "-m", f'"{initial_commit_msg}"', path=project_root)
    run_git_cmd("remote", "add", "origin", url, path=project_root)


def create_virtual_environment(
    project_root: str, name: str = ".venv", prompt: str = "{{cookiecutter.package}}"
) -> str:
    dest = path.join(project_root, name)
    run_python_cmd("virtualenv", dest, "--prompt", f'"({prompt}) "', module=True)
    return dest


def get_python_executable(virtual_environment: str) -> str:
    system = _system()
    if system in ("Linux", "Darwin"):
        return path.join(virtual_environment, "bin", "python")
    elif system == "Windows":
        return path.join(virtual_environment, "Scripts", "python.exe")
    else:
        raise RuntimeError(f"Unknown system {system}.")


def upgrade_pip_and_setuptools(python_executable: str) -> None:
    run_pip_cmd(
        "install", "--upgrade", "pip", "setuptools", python_executable=python_executable
    )


def install_dev_requirements(
    python_executable: str, project_root: str, file: str = "requirements-dev.txt"
) -> None:
    run_pip_cmd(
        "install",
        "-r",
        path.join(project_root, file),
        python_executable=python_executable,
    )


def main(project_root: str) -> None:
    initialize_git(project_root)

    try:
        virtual_environment = create_virtual_environment(project_root)
    except subprocess.CalledProcessError:
        warnings.warn("virtualenv is not available. Skipping initialization.")
        return

    python_executable = get_python_executable(virtual_environment)
    upgrade_pip_and_setuptools(python_executable)
    install_dev_requirements(python_executable, project_root)


if __name__ == "__main__":
    project_root = path.abspath(path.curdir)
    main(project_root)
