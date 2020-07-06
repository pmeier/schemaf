import itertools
import os
import re
from datetime import datetime
from importlib import import_module
from os import path
from setuptools import find_packages

import pytest

from .utils import load_module

PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), ".."))
PACKAGE_NAME = "{{cookiecutter.package}}"
PACKAGE_ROOT = path.join(PROJECT_ROOT, PACKAGE_NAME)


@pytest.fixture(scope="module")
def package_under_test():
    return load_module(PACKAGE_ROOT)


def test_import(subtests):
    def find_modules(dir, package=None):
        if package is not None:
            dir = path.join(dir, package.replace(".", os.sep))
        files = os.listdir(dir)
        modules = []
        for file in files:
            name, ext = path.splitext(file)
            if ext == ".py" and not name.startswith("_"):
                module = f"{package}." if package is not None else ""
                module += name
                modules.append(module)
        return modules

    public_packages = [
        package
        for package in find_packages(PACKAGE_ROOT)
        if not package.startswith("_")
    ]

    public_modules = find_modules(PACKAGE_ROOT)
    for package in public_packages:
        public_modules.extend(find_modules(PACKAGE_ROOT, package=package))

    for module in itertools.chain(public_packages, public_modules):
        with subtests.tests(module=module):
            import_module(f".{module}", package=PACKAGE_NAME)


def test_about(subtests, package_under_test):
    for attr in (
        "name",
        "description",
        "version",
        "keywords",
        "url",
        "license",
        "author",
        "author_email",
    ):
        with subtests.test(attr=attr):
            assert isinstance(getattr(package_under_test, f"__{attr}__"), str)


def test_name(package_under_test):
    assert package_under_test.__name__ == PACKAGE_NAME


def test_version(package_under_test):
    def is_canonical(version):
        # Copied from
        # https://www.python.org/dev/peps/pep-0440/#appendix-b-parsing-version-strings-with-regular-expressions
        return (
            re.match(
                r"^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$",
                version,
            )
            is not None
        )

    def is_dev(version):
        match = re.search(r"[.]dev\d+\+g[\da-f]{7}(?P<dirty>[.]d\d{14})?$", version)
        if match is None:
            return False

        dirty = match.group("dirty")
        if dirty is not None:
            try:
                datetime.strptime(dirty[2:], "%Y%m%d%H%M%S")
            except ValueError:
                return False

        return is_canonical(version[: match.span()[0]])

    version = package_under_test.__version__
    assert is_canonical(version) or is_dev(version)
