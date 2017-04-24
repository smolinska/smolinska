#!/usr/bin/env bash
source $(dirname "$0/")/config.sh

. /usr/share/virtualenvwrapper/virtualenvwrapper.sh
set -x
mkvirtualenv "$PROJECT_NAME" --python=`which python3.5 || which python3.4`
pip install -U pip
pip install -U setuptools
pip install -r requirements.txt
bower install --production

echo ok
