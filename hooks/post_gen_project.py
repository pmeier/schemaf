import subprocess
import sys
from os import path


def run_cmd(executable, *args):
    subprocess.check_call((executable, *args))


def run_python_cmd(*args, executable=sys.executable, module=False):
    if module:
        args = ("-m", *args)
    run_cmd(executable, *args)


def run_pip_cmd(*args, python_executable=sys.executable):
    run_python_cmd("pip", *args, executable=python_executable, module=True)


def run_git_cmd(*args, path=None):
    if path is not None:
        args = ("-C", path, *args)
    run_cmd("git", *args)


def initialize_git(
    project_root,
    user_name="{{cookiecutter.author}}",
    user_email="{{cookiecutter.author_email}}",
    initial_commit_msg="Initial commit",
    url="{{cookiecutter.url}}",
):
    run_git_cmd("init", project_root)
    run_git_cmd("config", "user.name", f"'{user_name}'", path=project_root)
    run_git_cmd("config", "user.email", f"'{user_email}'", path=project_root)
    run_git_cmd("add", ".", path=project_root)
    run_git_cmd("commit", "-m", initial_commit_msg, path=project_root)
    run_git_cmd("remote", "add", "origin", url, path=project_root)


def create_virtual_environment(
    project_root, name=".venv", prompt="{{cookiecutter.repo_name}}"
):
    dest = path.join(project_root, name)
    run_python_cmd("virtualenv", dest, "--prompt", f"({prompt}) ", module=True)
    return path.join(dest, "bin")


def install_package_as_editable(python_executable):
    run_pip_cmd("install", "--editable", ".", python_executable=python_executable)


def install_pre_commit_with_hooks(binary_dir, python_executable):
    run_pip_cmd("install", "pre-commit", python_executable=python_executable)

    pre_commit_executable = path.join(binary_dir, "pre-commit")
    run_cmd(pre_commit_executable, "install")


def main(project_root):
    initialize_git(project_root)
    binary_dir = create_virtual_environment(project_root)
    python_executable = path.join(binary_dir, "python")

    install_package_as_editable(python_executable)
    install_pre_commit_with_hooks(binary_dir, python_executable)


if __name__ == "__main__":
    project_root = path.abspath(path.curdir)
    main(project_root)
