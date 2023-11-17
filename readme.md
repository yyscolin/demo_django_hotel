# Demo Django Hotel

This is a simple web application powered by the Django framework, demonstrating
what a typical hotel website will look like.

## Setup
1. Clone the repo `git clone https://github.com/yyscolin/demo_django_hotel.git`
2. Create an empty database
3. Dump data into the database (Choose correct dump file in "database" folder)
4. Create a database user with SELECT, INSERT privileges
5. Copy project/settings.template.py to project/settings.py
6. Fill in the required information in the settings file

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
python3 \<project root\>/manage.py runserver 0:\<port\>
