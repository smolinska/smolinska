#!/usr/bin/env bash
cd $(dirname "$0/")
source ../config.sh
set -x

FIXTURE_DIR='apps/main/fixtures'

cd ../..
python manage.py loaddata user_data.json flats.json
