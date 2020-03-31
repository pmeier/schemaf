from importlib import import_module, util
import os
from os import path
import re
import itertools
from setuptools import find_packages
import unittest

PROJECT_ROOT = path.abspath(path.join(path.dirname(__file__), ".."))
PACKAGE_ROOT = path.join(PROJECT_ROOT, "{{cookiecutter.pkg_name}}")


def load_put():
    spec = util.spec_from_file_location(
        "{{cookiecutter.pkg_name}}", path.join(PACKAGE_ROOT, "__init__.py"),
    )
    put = util.module_from_spec(spec)
    spec.loader.exec_module(put)
    return put


package_under_test = load_put()


class TestCase(unittest.TestCase):
    def test_import(self):
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
            import_module(f".{module}", package=package_under_test)

    def test_about(self):
        for attr in (
            "name",
            "description",
            "version",
            "url",
            "license",
            "author",
            "author_email",
        ):
            self.assertIsInstance(getattr(package_under_test, f"__{attr}__"), str)

    def test_name(self):
        self.assertEqual(package_under_test.__name__, "{{cookiecutter.pkg_name}}")

    def test_version(self):
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

        self.assertTrue(is_canonical(package_under_test.__version__))