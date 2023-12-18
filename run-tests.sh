#!/bin/bash

set -e

OAREPO_VERSION=${OAREPO_VERSION:-11}

if test -d .venv-builder ; then
  rm -rf .venv-builder
fi

python3 -m venv .venv-builder
.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install -e .


BUILDER=.venv-builder/bin/oarepo-compile-model


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
pip install "oarepo[tests]==${OAREPO_VERSION}.*"
pip install -e 'tests/cf[tests]'
pip install pytest-invenio

pytest tests