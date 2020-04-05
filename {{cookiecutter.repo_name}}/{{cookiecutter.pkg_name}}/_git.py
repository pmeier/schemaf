from typing import Optional
from os import path
import subprocess

__all__ = ["is_repo", "is_available", "is_dirty", "hash"]


def is_repo(dir: str) -> bool:
    return path.exists(path.join(dir, ".git"))


def _run(*cmds: str, cwd: Optional[str] = None) -> str:
    return subprocess.check_output(("git", *cmds), cwd=cwd).decode("utf-8").strip()


def is_available() -> bool:
    try:
        _run("--help")
        return True
    except subprocess.CalledProcessError:
        return False
    except OSError:
        return False


def is_dirty(dir: str):
    return bool(_run("status", "-uno", "--porcelain", cwd=dir))


def hash(dir: str):
    return _run("rev-parse", "--short", "HEAD", cwd=dir)
