#!/usr/bin/env bash
source $(dirname "$0/")/config.sh

SOCKFILE="$PROD_LOCATION/$PROJECT_NAME.sock"      # we will communicte using this unix socket
USER=www-data                                     # the user to run as
GROUP=www-data                                    # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=project.settings.prod      # which settings file should Django use
DJANGO_WSGI_MODULE=project.wsgi                   # WSGI module name

echo "Starting $PROJECT_NAME as `whoami`"

# Activate the virtual environment
cd $PROD_LOCATION
source $VENV_PATH/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$PROD_LOCATION:$PYTHONPATH

# Create the run directory if it doesn't exist
#RUNDIR=$(dirname $SOCKFILE)
#test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $PROJECT_NAME \
  --workers $NUM_WORKERS \
  --log-level=critical \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE
