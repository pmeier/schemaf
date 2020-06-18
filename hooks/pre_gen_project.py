import re
import sys
from keyword import iskeyword


def verify(expr: bool, msg: str) -> None:
    if not expr:
        print(f"{msg.strip()} Aborting!")
        sys.exit(1)


def verify_pkg_name(pkg_name: str = "{{cookiecutter.repo_name}}") -> None:
    # Copied from
    # https://stackoverflow.com/a/36331242/1654607
    def is_valid_variable_name(name: str) -> bool:
        return name.isidentifier() and not iskeyword(name)

    verify(is_valid_variable_name(pkg_name), f"Package name {pkg_name} is not a valid.")


def verify_base_version(base_version: str = "{{cookiecutter.base_version}}") -> None:
    # Copied from
    # https://www.python.org/dev/peps/pep-0440/#appendix-b-parsing-version-strings-with-regular-expressions
    def is_canonical(version: str) -> bool:
        return (
            re.match(
                r"^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$",
                version,
            )
            is not None
        )

    verify(
        is_canonical(base_version), f"Base version {base_version} is not canonical.",
    )


def main() -> None:
    verify_pkg_name()
    verify_base_version()


if __name__ == "__main__":
    main()
