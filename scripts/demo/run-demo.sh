#!/usr/bin/env bash
cd $(dirname "$0/")
source ../config.sh
set +x
cd $DEMO_LOCATION
source $DEMO_VENV_PATH/bin/activate

python manage.py runserver --insecure --noreload "0.0.0.0:$DEMO_PORT" --settings=project.settings.demo >out.log 2>err.log &
echo "Project $PROJECT_NAME is running on http://$DEMO_HOST:$DEMO_PORT"
