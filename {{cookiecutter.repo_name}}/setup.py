from importlib.util import module_from_spec, spec_from_file_location
from os import path

from setuptools import find_packages, setup

PROJECT_ROOT = path.abspath(path.dirname(__file__))
PACKAGE_NAME = "{{cookiecutter.pkg_name}}"
PACKAGE_ROOT = path.join(PROJECT_ROOT, PACKAGE_NAME)


def load_git_module():
    spec = spec_from_file_location(PACKAGE_NAME, path.join(PACKAGE_ROOT, "_git.py"),)
    git = module_from_spec(spec)
    spec.loader.exec_module(git)
    return git


git = load_git_module()
about = {"git": git, "_PROJECT_ROOT": PROJECT_ROOT}
with open(path.join(PACKAGE_ROOT, "__about__.py"), "r") as fh:
    exec(fh.read(), about)

with open(path.join(PROJECT_ROOT, "README.md"), "r") as fh:
    long_description = fh.read()

install_requires = ("typing_extensions",)

type_check_requires = ("mypy",)

test_requires = ("pytest",)

doc_requires = (
    "sphinx",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
)

dev_requires = (
    *type_check_requires,
    *doc_requires,
    *test_requires,
    "pre-commit",
    "black",
)

extras_require = {
    "type_check": type_check_requires,
    "doc": doc_requires,
    "test": test_requires,
    "dev": dev_requires,
}

classifiers = (
    "Development Status :: {{cookiecutter.dev_status}}",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3 :: Only",
)

setup(
    name=about["__name__"],
    description=about["__description__"],
    version=about["__version__"],
    url=about["__url__"],
    license=about["__license__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(
        where=PROJECT_ROOT, exclude=("docs", "test", "third_party_stubs")
    ),
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">={{cookiecutter.minimum_python_version}}",
    classifiers=classifiers,
)
