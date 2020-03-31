from os import path
from setuptools import setup, find_packages

about = {}
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "{{cookiecutter.pkg_name}}", "__about__.py"), "r") as fh:
    exec(fh.read(), about)

with open(path.join(here, "README.md"), "r") as fh:
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
    packages=find_packages(where=here, exclude=("docs", "test", "third_party_stubs")),
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">={{cookiecutter.minimum_python_version}}",
    classifiers=classifiers,
)
