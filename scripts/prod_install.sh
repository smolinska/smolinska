#!/usr/bin/env bash
# this script is copied into production machine
set -x
set -o nounset
set -o errexit

mkdir -p "$PROD_LOCATION"
cd "$PROD_LOCATION"

git clone --branch "$PROJECT_NAME" --single-branch "$REPO_URL" .
git checkout "$PROJECT_NAME"
source scripts/config.sh

bower install --production
npm install coffee-script -g
sudo apt-get install ruby-sass
sudo apt-get install gettext

# Python
mkvirtualenv "$PROJECT_NAME" --python=`which python3.5`
pip install -U pip
pip install -U setuptools
pip install -r requirements.txt
pip install gunicorn
pip install setproctitle

echo "alias $PROJECT_NAME='cd $PROD_LOCATION && workon $PROJECT_NAME'" >> ~/.bashrc
echo "alias update-$PROJECT_NAME='$PROJECT_NAME &&\
 git fetch && git stash 'before update' && git reset origin/$PROJECT_NAME --hard && git stash pop &&\
 ./manage.py collectstatic --noinput'" >> ~/.bashrc

python manage.py migrate
python manage.py loaddata user_data.json
python manage.py compress --settings=project.settings.prod
python manage.py collectstatic
python manage.py compilemessages


# Permissions
sudo chown "$PROD_USER" -R .
sudo chgrp www-data -R .
sudo chmod g+rw -R static/CACHE
sudo chmod ug+rw .
sudo chmod ug+rw logs
sudo chmod ug+rw logs/*
sudo chmod ug+rw db.sqlite3


### sed configs VARS should be used without $ sign
CONF_VARS=$(grep scripts/config.sh -e = | awk -F= '{print $1}')
SUPERVISOR_CONF_FILE="scripts/output/$PROJECT_NAME.conf"
NGINX_SITE_CONF_FILE="scripts/output/$PROJECT_NAME"
mkdir scripts/output
cp scripts/supervisor "$SUPERVISOR_CONF_FILE"
cp scripts/nginx_conf "$NGINX_SITE_CONF_FILE"
for VAR in $CONF_VARS; do
    sed --in-place "s%$VAR%${!VAR}%g" "$SUPERVISOR_CONF_FILE"
    sed --in-place "s%$VAR%${!VAR}%g" "$NGINX_SITE_CONF_FILE"
done

# Supervisor
mkdir -p $PROD_LOCATION/logs/
touch "$PROD_LOCATION/logs/gunicorn_supervisor.log"
sudo cp "$SUPERVISOR_CONF_FILE" /etc/supervisor/conf.d/

# Nginx
sudo cp "$NGINX_SITE_CONF_FILE" /etc/nginx/sites-available/
ln -s "/etc/nginx/sites-available/$PROJECT_NAME" "/etc/nginx/sites-enabled/$PROJECT_NAME"

# Certificates
sudo cd /root
sudo git clone https://github.com/certbot/certbot
cd certbot
./certbot certonly --standalone -d "DOMAIN" -d "www.$DOMAIN" --agree-tos

sudo echo "/root/certbot/certbot-auto renew --standalone --pre-hook \"service nginx stop\" --post-hook \"service nginx start\" | mail -s \"Cert Renew at $PROJECT_NAME.pl\" kawalaaleksander@gmail.com" > /root/renew.sh
sudo {crontab -l -u root 2>/dev/null; echo "30 03 01 Feb,Apr,Jun,Aug,Oct,Dec * /root/renew.sh"} | sudo crontab -u root -

sudo service nginx restart


sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart "$PROJECT_NAME"

supervisorctl status