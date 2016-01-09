#!/usr/bin/env bash

source $(dirname "$0/")/config.sh
cd $DEMO_LOCATION
source $DEMO_VENV_PATH/bin/activate

echo "Project $PROJECT_NAME is starting on http://$DEMO_HOST:$DEMO_PORT"
exec python manage.py runserver --insecure --noreload "0.0.0.0:$DEMO_PORT" --settings=project.settings.demo
