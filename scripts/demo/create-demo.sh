#!/usr/bin/env bash
cd $(dirname "$0/")
source ../config.sh
set -x

ssh -p "$DEMO_SSH_PORT" -t "$DEMO_USER_HOST" "set -x; \
mkdir -p $DEMO_LOCATION; \
cd $DEMO_LOCATION; \
git clone --branch "$PROJECT_NAME" --single-branch "$REPO_URL" .; \
chmod u+x -R ./scripts; \
export DJANGO_SETTINGS_MODULE='project.settings.demo'; \
./scripts/start_auto.sh; \
./scripts/post_pull.sh; \
./scripts/demo/run-demo.sh;"