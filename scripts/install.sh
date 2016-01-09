#!/usr/bin/env bash
cd $(dirname "$0/")
source base.sh

### Prepare bare new virtual machine for deployments
SCRIPT_TO_RUN='prod_prepare.sh'
set -x

scp -P "$SSH_PORT" "scripts/$SCRIPT_TO_RUN" 'scripts/nginx.conf' '~/.vimrc' '~/.gitconfig' "$FIRST_USER@$PROD_HOST:~/"
ssh -t -p "$SSH_PORT" "$FIRST_USER@$PROD_HOST" "export EMAIL=$EMAIL; su root; ~/$SCRIPT_TO_RUN"

## easy access
ssh-copy-id -p "$SSH_PORT" "$PROD_USER_HOST"
echo "alias $PROJECT_NAME='ssh -p $SSH_PORT $PROD_USER_HOST'" >> ~/.bashrc



exit

### Deploy another site on prepared production

SCRIPT_NAME='prod_install.sh'
SCRIPT_TO_RUN="install_script_$PROJECT_NAME"

scp -P "$SSH_PORT" "scripts/$SCRIPT_NAME" "$PROD_USER_HOST:~/$SCRIPT_TO_RUN"
ssh -t -p "$SSH_PORT" "$PROD_USER_HOST" "\
 export PROJECT_NAME=$PROJECT_NAME;\
 export REPO_URL=$REPO_URL;\
 export PROD_LOCATION=$PROD_LOCATION;\
 ~/$SCRIPT_TO_RUN"

