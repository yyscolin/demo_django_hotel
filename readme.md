# Demo Django Hotel

This is a simple web application powered by the Django framework, demonstrating what a typical hotel website will look like.

## Setup
1. Clone the repo `git clone https://github.com/yyscolin/demo_django_hotel.git`
2. Create an empty database
3. Dump data into the database (Choose correct dump file in "database" folder)
4. Create a database user to access database information
5. Copy project/settings.template.py to project/settings.py
6. Fill in the required information in the settings file

### Required Linux packages
python3-django python-django-common postgresql postgresql-contrib libpq-dev python-dev default-libmysqlclient-dev

### Database Privileges Requirement
SELECT, INSERT, UPDATE, DELETE

### Start running the app
python3 <project root>/manage.py runserver 0:<port>
