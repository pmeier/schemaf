#!/usr/bin/env sh

pip3 install .

pip3 install --upgrade -r requirements-test.txt
pip3 install codecov

pip3 list
