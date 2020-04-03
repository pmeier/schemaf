[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Build Status](https://travis-ci.org/pmeier/schemaf.svg?branch=master)](https://travis-ci.org/pmeier/schemaf)

# schemaf

This is my personal [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) for FOSS Python projects on [`GitHub`](https://github.com/). The name is based on the [german translation](https://www.dict.cc/?s=to+use+a+cookie-cutter+approach) "_zu **Schema F** greifen_" of the englisch phrase "_to use a cookie-cutter approach_".

The created skeleton comprises an installable Python package with smoke tests and an empty documentation. Furthermore, it is ready to be activated on [Travis CI](https://travis-ci.org) and [Read the Docs](https://readthedocs.org/). The CI test also comprises checks for code format with [`black`](https://github.com/psf/black) as well as static type annotations with [`mypy`](http://mypy-lang.org/). 

## Usage

1. Install `cookiecutter` with `pip install cookiecutter`
2. Run `cookiecutter https://github.com/pmeier/schemaf`
3. Create an empty [GitHub repository](https://github.com/new). The name should match the `{{cookiecutter.repo_name}}` variable. The repository has to be public.
4. Activate the project on [Travis CI](https://travis-ci.org/account/repositories). You may need to synchronize your account before the new repository shows up.
5. Run `git push -u origin master` inside the new repository.
6. Activate the project on [Read the Docs](https://readthedocs.org/dashboard/import/). You may need to synchronize your account before the new repository shows up.
