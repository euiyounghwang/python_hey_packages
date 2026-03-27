#!/bin/bash
set -e

# Activate virtualenv && run serivce

# cd /Users/euiyoung.hwang/ES/Python_Workspace/python-django
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd $SCRIPTDIR
echo $PWD

VENV=".test"

# Python 3.11.7 with Window
if [ -d "$VENV/bin" ]; then
    source $SCRIPTDIR/$VENV/bin/activate
else
    source $SCRIPTDIR/$VENV/Scripts/activate
fi

export PYTHONDONTWRITEBYTECODE=1

# py.test -v tests
# poetry run py.test -v --junitxml=test-reports/junit/pytest.xml --cov-report html --cov tests/
pytest -v --cov ./tests