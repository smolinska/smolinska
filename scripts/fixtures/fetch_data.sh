#!/usr/bin/env bash
cd $(dirname "$0/")
source ../config.sh
set -x

FIXTURE_DIR='apps/main/fixtures'
cd ..

ssh -p "$SSH_PORT" -t "$PROD_USER_HOST" "set -x; cd $PROD_LOCATION; workon $PROJECT_NAME; ./manage.py save;"
scp -P "$SSH_PORT" "$PROD_USER_HOST:$PROD_LOCATION/$FIXTURE_DIR/*" "$FIXTURE_DIR/"
