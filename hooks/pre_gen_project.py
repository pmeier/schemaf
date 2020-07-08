import sys
from keyword import iskeyword


def verify_pkg_name(pkg_name: str = "{{cookiecutter.package}}") -> None:
    # Copied from
    # https://stackoverflow.com/a/36331242/1654607
    def is_valid_variable_name(name: str) -> bool:
        return name.isidentifier() and not iskeyword(name)

    if not is_valid_variable_name(pkg_name):
        print(f"Package name {pkg_name} is not a valid. Aborting!")
        sys.exit(1)


def main() -> None:
    verify_pkg_name()


if __name__ == "__main__":
    main()
