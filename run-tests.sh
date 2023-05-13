#!/bin/bash

set -e

python3 -m venv .venv
.venv/bin/pip install -U setuptools pip wheel
.venv/bin/pip install -e .


BUILDER=.venv/bin/oarepo-compile-model


if true ; then
    test -d tests/cf && rm -rf tests/cf
    ${BUILDER} tests/cf.yaml --output-directory tests/cf -vvv
fi


python3 -m venv .venv-tests
source .venv-tests/bin/activate

pip install -U setuptools pip wheel
pip install pyyaml opensearch-dsl 
pip install -e tests/cf
pip install pytest-invenio

pytest tests