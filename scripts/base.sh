#!/usr/bin/env bash
#base.sh -- it should be sourced from other scripts. It sets working dir to project basedir
source config.sh

if [[ "$VIRTUAL_ENV" != */$USED_VIRTUAL_ENV ]]
then
    workon "$USED_VIRTUAL_ENV"
fi

cd ..

set -o nounset
set -o errexit
