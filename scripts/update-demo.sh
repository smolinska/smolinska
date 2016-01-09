#!/usr/bin/env bash
cd $(dirname "$0/")
source config.sh
set -x

ssh -p "$DEMO_SSH_PORT" -t "$DEMO_USER_HOST" "set -x; cd $DEMO_LOCATION; git fetch; git reset origin/$BRANCH --hard; ./scripts/post_pull.sh;"
