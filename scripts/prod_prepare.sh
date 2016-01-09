#!/usr/bin/env bash

### SYSTEM CONFIG
# libjpeg-dev zlib1g-dev are required for pillow to work properrly

apt-get update
apt-get install man-db htop vim sudo tree git python3 python3-pip python3-dev virtualenvwrapper libjpeg-dev zlib1g-dev nginx-extras nginx supervisor


exit # Unchecked commands

adduser bond
vim /etc/ssh/sshd_config  # PermitRootLogin no  # Port 2223
service sshd restart


# Generate ssh key for git
ssh-keygen -t rsa -b 4096 -C "$EMAIL"
echo '#################################'
echo
cat ~/.ssh/id_rsa.pub
echo
echo '#################################'
echo 'add production key to repo'
read -p 'Press any key to continue'