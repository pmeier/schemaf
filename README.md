[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
[![Build Status](https://travis-ci.org/pmeier/schemaf.svg?branch=master)](https://travis-ci.org/pmeier/schemaf)


# schemaf

This is my personal [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) for FOSS Python projects on [`GitHub`](https://github.com/). The name is based on the [german translation](https://www.dict.cc/?s=to+use+a+cookie-cutter+approach) "_zu **Schema F** greifen_" of the english phrase "_to use a cookie-cutter approach_".

The created project comprises an installable but empty Python package with smoke tests and an empty documentation. 

CI is enabled and comprises these features:

- Code format ([`isort`](https://timothycrosley.github.io/isort/), [`black`](https://github.com/psf/black) and [`flake8`](https://flake8.pycqa.org/en/latest/)) and static typing ([`mypy`](http://mypy-lang.org/)) is checked via [GitHub Actions](https://github.com/features/actions).
- Tests on Linux and macOs are run on [Travis CI](https://travis-ci.com)
- Tests on Windows are run on [AppVeyor](https://www.appveyor.com/)
- Docs are built and hosted on [Read the Docs](https://readthedocs.org)


## Usage

1. Install `cookiecutter` with `pip install cookiecutter`
2. Run `cookiecutter https://github.com/pmeier/schemaf`
3. Create an empty [GitHub repository](https://github.com/new). 
    - The name should match the `{{cookiecutter.repo_name}}` variable. 
    - The repository has to be public.
    - You need to grant TravisCI access to the repository 
4. Run `git push --set-upstream origin master` inside the new repository.
5. Activate the project on [Read the Docs](https://readthedocs.org/dashboard/import/). You may need to synchronize your account before the new repository shows up.


## Post-installation actions

Navigate to project `Settings`

1. Navigate to `Options`
    - `Features`
        - Uncheck `Wikis`
        - Uncheck `Projects`
    - `Merge button`
        - Uncheck `Allow merge commits`
        - Uncheck `Allow rebase commits`
        - Check `Automatically delete head branches`
2. Navigate to `Branches`
    - `Add rule` to `Branch protection rules`
        - `Branch name pattern`: `master`
        - Check `Requires status checks to pass before merging` and all sub items
        - Check `Require signed commits`
