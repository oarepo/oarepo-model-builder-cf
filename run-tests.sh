#!/bin/bash

set -e

if test -d .venv ; then
  rm -rf .venv
fi

python3 -m venv .venv
.venv/bin/pip install -U setuptools pip wheel
.venv/bin/pip install -e .


BUILDER=.venv/bin/oarepo-compile-model


if test -d tests/cf ; then
  rm -rf tests/cf
fi
${BUILDER} tests/cf.yaml --output-directory tests/cf -vvv

if test -d .venv-tests ; then
  rm -rf .venv-tests
fi

python3 -m venv .venv-tests
source .venv-tests/bin/activate

pip install -U setuptools pip wheel
pip install -e 'tests/cf[tests]'
pip install pytest-invenio

pytest tests