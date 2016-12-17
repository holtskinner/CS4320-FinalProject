# CS4320-FinalProject
## Software Engineering Team 4
Hofer, Skinner, Raza, Zhang, Rogers, Pudotha

# Deployment

1. Sign in an Amazon Web Service Account, and launch an EC2 Ubuntu Server 16.04 LTS instance.
2. In the Ubuntu Server terminal, clone code from repository.
```
git clone 'https://github.com/holtwashere/CS4320-FinalProject'
```

Run the following command to install necessary components, and allow all of the installations.

```
sudo ./deployment.sh
```
Then complete the following steps

Deploying a flask application is quite tricky.
First make sure that you have installed apache2 and mongoDB.

The next step is to install flask:
```
pip install Flask
```

Next make a directory called "flask-dev".
The content of this directory will be populated with every file in the Source folder on the git repo.

ec2-35-164-234-183.us-west-2.compute.amazonaws.com

Open the host file:

```
vim /etc/hosts
```

Paste this line on top:
```
127.0.0.1 ec2-35-164-234-183.us-west-2.compute.amazonaws.com
```

This will direct the url to run the application that is running on the server

Navigate to:
```
cd /etc/apache2/sites-available/
```

Make a file called "myapp.conf"

The content of this file will be:

```
<virtualhost *:80>
    ServerName ec2-35-164-234-183.us-west-2.compute.amazonaws.com

    WSGIDaemonProcess webtool user=flask group=www-data threads=5 home=/var/www/flask-dev/
    WSGIScriptAlias / /var/www/flask-dev/myapp.wsgi

    <directory /var/www/flask-dev>
        WSGIProcessGroup webtool
        WSGIApplicationGroup %{GLOBAL}
        WSGIScriptReloading On
        Order deny,allow
        Allow from all
    </directory>
</virtualhost>
```

Enable the virual host:
```
  sudo a2ensite myapp.conf
```

Restart Apache:
```
  sudo /etc/init.d/apache2 restart
```


## The website can be accessed through the default public DNS.

http://ec2-35-164-234-183.us-west-2.compute.amazonaws.com/
