from os import path
from setuptools import find_packages, setup

PROJECT_ROOT = path.abspath(path.dirname(__file__))
PACKAGE_NAME = "{{cookiecutter.package}}"
PACKAGE_ROOT = path.join(PROJECT_ROOT, PACKAGE_NAME)


about = {}
with open(path.join(PACKAGE_ROOT, "__about__.py"), "r") as fh:
    exec(fh.read(), about)

with open(path.join(PROJECT_ROOT, "README.rst"), "r") as fh:
    long_description = fh.read()

package_data = {PACKAGE_NAME: ["py.typed"]}

classifiers = [
    "Development Status :: {{cookiecutter.dev_status}}",
    "License :: OSI Approved :: BSD License",
    {%- for minor in range(cookiecutter.min_python_version[-1]|int, cookiecutter.max_python_version[-1]|int + 1) %}
    "Programming Language :: Python :: 3.{{minor}}",
    {%- endfor %}
    "Typing :: Typed",
]

setup(
    name=about["__name__"],
    description=about["__description__"],
    keywords=about["__keywords__"],
    url=about["__url__"],
    license=about["__license__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=find_packages(where=PROJECT_ROOT, exclude=("docs", "tests", ".github")),
    package_data=package_data,
    python_requires=">={{cookiecutter.min_python_version}}",
    classifiers=classifiers,
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "write_to": path.join(PACKAGE_ROOT, "_version.py"),
        "version_scheme": "release-branch-semver",
        "local_scheme": "node-and-timestamp",
    },
)
