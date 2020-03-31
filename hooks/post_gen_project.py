import sys
from os import path
import subprocess


def run_cmd(executable, *args):
    subprocess.check_call((executable, *args))


def run_python_cmd(*args, executable=sys.executable, module=False):
    if module:
        args = ("-m", *args)
    run_cmd(executable, *args)


def initialize_git(project_root):
    run_cmd("git", "init", project_root)


def create_virtual_environment(
    project_root, name=".venv", prompt="{{cookiecutter.repo_name}}"
):
    dest = path.join(project_root, name)
    run_python_cmd("virtualenv", dest, "--prompt", f"({prompt}) ", module=True)
    return path.join(dest, "bin")


def install_package_with_dev_requirements(executable):
    run_python_cmd("pip", "install", "-e", ".[dev]", executable=executable, module=True)


def install_pre_commit_hooks(executable):
    run_cmd(executable, "install")


def main(project_root):
    initialize_git(project_root)
    binary_dir = create_virtual_environment(project_root)
    python_executable = path.join(binary_dir, "python")

    install_package_with_dev_requirements(python_executable)
    install_pre_commit_hooks(path.join(binary_dir, "pre-commit"))


if __name__ == "__main__":
    project_root = path.abspath(path.curdir)
    main(project_root)
