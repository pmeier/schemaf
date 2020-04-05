from keyword import iskeyword
import sys
import re


def verify(expr, msg):
    if not expr:
        print(f"{msg.strip()} Aborting!")
        sys.exit(1)


def verify_pkg_name(pkg_name="{{cookiecutter.pkg_name}}"):
    # Copied from
    # https://stackoverflow.com/a/36331242/1654607
    def is_valid_variable_name(name):
        return name.isidentifier() and not iskeyword(name)

    verify(is_valid_variable_name(pkg_name), f"Package name {pkg_name} is not a valid.")


def verify_version(version="{{cookiecutter.version}}"):
    # Copied from
    # https://www.python.org/dev/peps/pep-0440/#appendix-b-parsing-version-strings-with-regular-expressions
    def is_canonical(version):
        return (
            re.match(
                r"^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$",
                version,
            )
            is not None
        )

    def is_dev(version):
        match = re.search(r"\+dev([.][\da-f]{7}([.]dirty)?)?$", version)
        if match is not None:
            return is_canonical(version[: match.span()[0]])
        else:
            return False

    verify(
        is_canonical(version) or is_dev(version),
        f"Version {version} is not canonical nor dev.",
    )


def main():
    verify_pkg_name()
    verify_version()


if __name__ == "__main__":
    main()
