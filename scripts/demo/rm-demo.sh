#!/usr/bin/env bash
cd $(dirname "$0/")
source ../config.sh
set -x

ssh -p "$DEMO_SSH_PORT" -t "$DEMO_USER_HOST" ". /usr/share/virtualenvwrapper/virtualenvwrapper.sh; set -x; \
rmvirtualenv "$PROJECT_NAME"; rm -rf $DEMO_LOCATION;"