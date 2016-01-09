#!/usr/bin/env bash
# config.sh -- it is sourced from base.sh. It only sets variables.
# WARNING: don't use % in variebles or change sed delimiter

PROJECT_NAME='glenrys'
DOMAIN='glenrys.pl'
FIRST_USER='root'
PROD_USER='bond'
PROD_HOST='alpakara.pl'
SSH_PORT=21022
USED_VIRTUAL_ENV="$PROJECT_NAME"
REPO_URL='git@bitbucket.org:BondxD/django-sites.git'
EMAIL='kawalaaleksander@gmail.com'

PROD_LOCATION="/var/www/$PROJECT_NAME"
VENV_PATH="/home/$PROD_USER/.virtualenvs/$PROJECT_NAME"
PROD_USER_HOST="$PROD_USER@$PROD_HOST"
FIXTURE_DIR='apps/main/fixtures'
BRANCH="$PROJECT_NAME"

DEMO_SSH_PORT=21022
DEMO_HOST="alpakara.pl"
DEMO_USER='alex'
DEMO_USER_HOST="$DEMO_USER@$DEMO_HOST"
DEMO_LOCATION="/var/www/demo/$PROJECT_NAME"
DEMO_VENV_PATH="/home/$DEMO_USER/.virtualenvs/$PROJECT_NAME"
DEMO_PORT=1214
