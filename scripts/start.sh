#!/usr/bin/env bash
source $(dirname "$0/")/config.sh

read -p "Remember to edit project name in config.sh [Y/n]" -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]
then
    git co -b "$PROJECT_NAME"

    ./scripts/start_auto.sh

    python manage.py migrate
    python manage.py load

    filelines=`cat requirements.txt`
    truncate requirements.txt --size 0
    pip freeze | grep Django >> requirements.txt
    for r in $filelines
    do
        pip freeze | grep "$r==" >> requirements.txt
    done

    git ci -am "$PROJECT_NAME initial"
    echo ok
fi
