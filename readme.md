# Demo Django Hotel

Experience an elegant web application showcasing the capabilities of Django
framework, designed to emulate the essence of a modern hotel website.

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
- pip3 packages:
    - Update pip3 (optional) `python3 -m pip install --upgrade pip`
    - Install virtualenv (if not yet installed) `apt install python3-virtualenv`
    - Go to project root `cd <project root>`
    - Create virtualenv `virtualenv env`
    - Start virtualenv (Windows) `.\env\Scripts\activate`
    - Start virtualenv (Linux) `source env/bin/activate`
    - Install pip dependencies `pip3 install -r requirements.txt`

### Required Linux packages
```
# django
apt install python3-django python-django-common

# postgresql
apt install postgresql postgresql-contrib

# mysql
apt install pkg-config default-libmysqlclient-dev
```

## On Microsoft Azure App Service

### Static file issue
Due to Azure not serving static files with Django properly, a PHP App Service
will be used as a proxy. In this PHP App Service's server:
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
`py manage.py runserver 0:8080`
