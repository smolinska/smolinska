#!/usr/bin/env bash
cd $(dirname "$0/")
source config.sh
cd ..

set +x
. /usr/share/virtualenvwrapper/virtualenvwrapper.sh
set -x
workon "$USED_VIRTUAL_ENV"

python manage.py migrate
python manage.py load
python manage.py compilemessages
python manage.py collectstatic --no-input