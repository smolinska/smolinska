#!/usr/bin/env bash
cd $(dirname "$0/")
source ../base.sh
set -x

FIXTURE_DIR='apps/main/fixtures'
FIXTURE_FILE='user_data.json'

./manage.py save
scp -P "$SSH_PORT" "$FIXTURE_DIR/$FIXTURE_FILE" "$PROD_USER_HOST:$PROD_LOCATION/"
ssh -p "$SSH_PORT" -t "$PROD_USER_HOST" "set -x; cd $PROD_LOCATION; workon $PROJECT_NAME; ./manage.py load; rm $FIXTURE_FILE;"
