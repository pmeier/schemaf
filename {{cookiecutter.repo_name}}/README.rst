{{cookiecutter.pkg_name}}
========================

{{cookiecutter.description}}

.. start-badges

.. list-table::
    :stub-columns: 1

    * - package
      - |license| |status|
    * - code
      - |black| |mypy| |lint|
    * - tests
      - |linux_macos| |windows| |coverage|
    * - docs
      - |docs| |rtd|

.. end-badges

For installation instructions and usage examples please consult the documentation
`hosted on readthedocs.com <https://{{cookiecutter.pkg_name}}.readthedocs.io/en/latest>`_ .

.. |license|
  image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :target: https://opensource.org/licenses/BSD-3-Clause
    :alt: License

.. |status|
  image:: https://www.repostatus.org/badges/latest/wip.svg
    :alt: Project Status: WIP
    :target: https://www.repostatus.org/#wip

.. |black|
  image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black
   
.. |mypy|
  image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: http://mypy-lang.org/
    :alt: mypy

.. |lint|
  image:: https://github.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/workflows/lint/badge.svg
    :target: https://github.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/actions?query=workflow%3Alint+branch%3Amaster
    :alt: Lint status via GitHub Actions

.. |linux_macos|
  image:: https://img.shields.io/travis/com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}?label=Linux%20%2F%20macOS&logo=Travis
    :target: https://travis-ci.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}
    :alt: Test status on Linux and macOS via Travis CI

.. |windows|
  image:: https://img.shields.io/appveyor/build/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name.replace("_", "-")}}?label=Windows&logo=AppVeyor
    :target: https://ci.appveyor.com/project/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name.replace("_", "-")}}
    :alt: Test status on Windows via AppVeyor
   
.. |coverage|
  image:: https://codecov.io/gh/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}
    :alt: Test coverage

.. |docs|
  image:: https://github.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/workflows/docs/badge.svg
    :target: https://github.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/actions?query=workflow%3Adocs+branch%3Amaster
    :alt: Docs status via GitHub Actions

.. |rtd|
  image:: https://img.shields.io/readthedocs/{{cookiecutter.pkg_name.replace("_", "-")}}?label=latest&logo=read%20the%20docs
    :target: https://{{cookiecutter.pkg_name.replace("_", "-")}}.readthedocs.io/en/latest/?badge=latest
    :alt: Latest documentation hosted on Read the Docs
