#!/bin/bash
echo 'enter the password'
sudo -i
# install apache2, python, mongo driver, and mongodb
apt-get update
apt-get -y install apache2
apt-get install python
apt-get install python-setuptools
easy_install pymongo
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
apt-get update
apt-get install -y mongodb-org
service apache2 reload
exit
# move website to local host 
mv /Source/* /var/www/html/
