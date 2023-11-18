# Demo Django Hotel

This is a simple web application powered by the Django framework, demonstrating
what a typical hotel website will look like.

## Setup
- Clone the repo `git clone https://github.com/yyscolin/demo_django_hotel.git`
- Copy project/settings.template.py to project/settings.py
- Fill in the required information in the settings file
    - Ensure that the database user has full privileges
- Create an empty database
- Create table structures with `py manage.py migrate`
- Dump data from database.sql into the database
- Create a database user with SELECT, INSERT privileges
- Update the database user in project/settings.py to the newly created user

### Required Linux packages
python3-django python-django-common postgresql postgresql-contrib libpq-dev python-dev default-libmysqlclient-dev

## Deployment to Microsoft Azure App Service
- Install apt packages `apt install pkg-config`
- Install virtualenv `pip3 install venv`
- Go to project root `cd /home/site/wwwroot`
- Create venv `virtualenv env`
- Start venv `source env/bin/activate`
- Install pip dependencies `pip3 install -r requirements.txt`

### Static file issue
Due to Azure not serving static files with Django properly, a PHP App Service
will be used as a proxy.
- Create a copy of the nginx config file
`cp /etc/nginx/sites-available/default /home/nginx.conf`
- Edit the copied nginx.conf file and replace the `location /` part with the
following lines
```
    location /static {}

    location / {
        proxy_pass <app server's URL>;
    }
```
- Create a folder for static files `mkdir /home/site/wwwroot/static`
- Upload all contents in resources folder to /home/site/wwwroot/static via FTPS
- In the server's Settings - Configuration > General Settings > Startup
Command, enter the following code
```
cp /home/nginx.conf /etc/nginx/sites-available/default; service nginx restart
```

## Start running the app
`py manage.py runserver 0:\<port\>`
