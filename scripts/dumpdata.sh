#!/usr/bin/env bash
cd $(dirname "$0/")
source config.sh
set -x

FIXTURE_DIR='apps/main/fixtures'

cd ..
python manage.py dumpdata --output "$FIXTURE_DIR/user_data.json" --indent 2 main.MenuItem main.orderedmodelex
python manage.py dumpdata --output "$FIXTURE_DIR/flats.json" --indent 2 main.FlatType main.Room main.Flat
