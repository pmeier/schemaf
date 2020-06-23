[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) 
[![cookiecutter](https://github.com/pmeier/schemaf/workflows/cookiecutter/badge.svg)](https://github.com/pmeier/schemaf/actions?query=workflow%3Acookiecutter)
[![cookie](https://github.com/pmeier/schemaf/workflows/cookie/badge.svg)](https://github.com/pmeier/schemaf/actions?query=workflow%3Acookie)


# schemaf

This is my personal [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) for FOSS Python projects on [`GitHub`](https://github.com/). The name is based on the [german translation](https://www.dict.cc/?s=to+use+a+cookie-cutter+approach) "_zu **Schema F** greifen_" of the english phrase "_to use a cookie-cutter approach_".

The created project comprises an installable but empty Python package with smoke tests and an empty documentation. 

CI is enabled and comprises these features:

- Code format ([`isort`](https://timothycrosley.github.io/isort/), [`black`](https://github.com/psf/black) and [`flake8`](https://flake8.pycqa.org/en/latest/)) and static typing ([`mypy`](http://mypy-lang.org/)) is checked for every PR via [GitHub Actions](https://github.com/features/actions).
- Tests are run for every PR for `python3.[6-8]` on Linux, Windows, and macOS via [GitHub Actions](https://github.com/features/actions).
- Docs are checked for every PR via [GitHub Actions](https://github.com/features/actions) and hosted on [Read the Docs](https://readthedocs.org)
- Everytime a branch is pushed to `releases/*` it is checked if it is publishable by uploading it to [TestPyPI](https://test.pypi.org/). If a release is created via GitHub, it is uploaded to [PyPI](https://pypi.org/). Make sure to set 
  - `TESTPYPI_USERNAME`
  - `TESTPYPI_PASSWORD`
  - `PYPI_USERNAME`
  - `PYPI_PASSWORD`
  
  in `Settings/Secrets`.

## Usage

1. Install `cookiecutter` with `pip install cookiecutter`
2. Run `cookiecutter https://github.com/pmeier/schemaf`
3. Create an empty [GitHub repository](https://github.com/new). 
    - The name should match the `{{cookiecutter.package}}` variable. 
    - The repository has to be public.
5. Run `git push --set-upstream origin master` inside the new repository.
6. Activate the project on [Read the Docs](https://readthedocs.org/dashboard/import/). You may need to synchronize your account before the new repository shows up.


## Post-installation actions

Navigate to project `Settings/Options`
- `Features`
  - Uncheck `Wikis`
  - Uncheck `Projects`
- `Merge button`
  - Uncheck `Allow merge commits`
  - Uncheck `Allow rebase commits`
  - Check `Automatically delete head branches`
