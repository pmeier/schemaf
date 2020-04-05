from os import path

__all__ = [
    "__name__",
    "__description__",
    "__version__",
    "__url__",
    "__license__",
    "__author__",
    "__author_email__",
]

__name__ = "{{cookiecutter.pkg_name}}"
__description__ = "{{cookiecutter.description}}"
__version__ = "{{cookiecutter.version}}"
__url__ = "{{cookiecutter.url}}"
__license__ = "BSD 3-Clause"
__author__ = "{{cookiecutter.author}}"
__author_email__ = "{{cookiecutter.author_email}}"

_IS_DEV_VERSION = __version__.endswith("+dev")

if "git" not in globals():
    from . import _git as git

if "_PROJECT_ROOT" not in globals():
    _PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), ".."))

if _IS_DEV_VERSION and git.is_available() and git.is_repo(_PROJECT_ROOT):
    __version__ += f".{git.hash(_PROJECT_ROOT)}"
    if git.is_dirty(_PROJECT_ROOT):
        __version__ += ".dirty"
