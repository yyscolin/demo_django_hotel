# Git clone
cd /srv
sudo git clone https://github.com/yyscolin/demo_django_hotel.git
sudo chown user:group demo_django_hotel

# Install dependencies
sudo apt install -y python3-pip python-django-common python3-django postgresql postgresql-contrib libpq-dev python-dev
pip3 install Django psycopg2

# Database Setup
sudo -u postgres psql
CREATE USER PRJHDD WITH PASSWORD =NNjHrq+zx%6@Uz+;
CREATE DATABASE demo_django_hotel;
ctrl+d to exit

# Sql Dump
sudo -u postgres psql -d demo_django_hotel < ddh.sql

# Grant Privileges
sudo -u postgres psql
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA demo_django_hotel TO PRJHDD;
ctrl+d to exit

# Start running the app
python3 /srv/demo_django_hotel/manage.py runserver 0:8080
