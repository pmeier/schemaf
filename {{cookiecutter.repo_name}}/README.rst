{{cookiecutter.pkg_name}}
========================

{{cookiecutter.description}}

.. start-badges

.. list-table::
    :stub-columns: 1

    * - package
      - |license| |status|
    * - code
      - |black| |code_format| |mypy| |static_typing|
    * - tests
      - |linux_macos| |windows| |coverage|
    * - docs
      - |docs|

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

.. |code_format|
  image:: https://github.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/workflows/Code%20format/badge.svg
    :alt: Code format status via GitHub Actions
   
.. |mypy|
  image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: http://mypy-lang.org/
    :alt: mypy
   
.. |static_typing|
  image:: https://github.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/workflows/Static%20typing/badge.svg
    :alt: Static typing status via GitHub Actions

.. |linux_macos|
  image:: https://img.shields.io/travis/com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}?label=Linux%20%2F%20macOS
    :target: https://travis-ci.com/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}
    :alt: Test status on Linux and macOS via Travis CI

.. |windows|
  image:: https://img.shields.io/appveyor/build/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}?label=Windows
    :target: FIXME
    :alt: Test status on Windows via AppVeyor
   
.. |coverage|
  image:: https://codecov.io/gh/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{cookiecutter.github_tag}}/{{cookiecutter.pkg_name}}
    :alt: Test coverage
   
.. |docs|
  image:: https://readthedocs.org/projects/{{cookiecutter.pkg_name}}/badge/?version=latest
    :target: https://{{cookiecutter.pkg_name}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation status