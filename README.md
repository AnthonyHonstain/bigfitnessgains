BigFitnessGains
===========
Django webapp for tracking workout goals. http://bigfitnessgains.herokuapp.com/

#### User facing pages
* landing page - http://bigfitnessgains.herokuapp.com/ 
* signup - http://bigfitnessgains.herokuapp.com/accounts/signup 
 * RESULT - directed to http://bigfitnessgains.herokuapp.com/accounts/test_ant/signup/complete/ 
 * RESULT - email should be delivered where you can activate your account, contains email link which should take you to your profile page.
* profile page - http://bigfitnessgains.herokuapp.com/accounts/<YOUR ACCOUNT NAME HERE>/
* Admin Pages - http://bigfitnessgains.herokuapp.com/admin/
 * From here you can manage the profiles

#### Important References
These are the third party apps of great importance to this project, links are provided below>

* userena - third party app for handling user profiles
 * userena - http://docs.django-userena.org/en/latest/installation.html
 * userena github - https://github.com/bread-and-pepper/django-userena

* Django REST Framework
 * http://www.django-rest-framework.org/

* South - database migrations
 * http://south.readthedocs.org/en/latest/whataremigrations.html
 * Tutorial - http://south.readthedocs.org/en/latest/tutorial/part1.html#tutorial-part-1

Initial Dev Env Setup
===========

#### Virtualenv
Get virtualenv, create an environment to work in, and activate your terminal.
```
sudo apt-get install python-virtualenv
virtualenv workout_env --no-site-packages
cd workout_env/
workout_env$ source bin/activate
```
NOTE - you need to run this command every time you have a new terminal you want to work with the project:
```
cd workout_env/
source bin/activate
```

#### Dependencies
Install Required Dependencies
* This part is manual - the rest of the python dependencies will be installed automatically using pip in the next step.
```
sudo apt-get install python-dev build-essential libpq-dev libevent-dev libmemcached-dev postgresql-client node-less
```

Install Python Project Dependencies
* There is a dev and prod version with slightly different dependencies, also notice there is a common.txt with dependencies for both.
```
pip install -r reqs/dev.txt
```

#### Database
* We are using PostgreSQL for this project - in dev and in production.

First time - install postgresql with ubuntu. Example error: *createdb: could not connect to database template1: FATAL:  role "YOUR_USER_NAME" does not exist*
```
sudo su
su postgres
createuser --interactive
```

Create and setup the DB to run locally (run from the django directory that contains manage.py).
```
createdb -E utf-8 -e bigfitnessgains
```

Populating the database
```
cd bigfitnessgains/apps/mainapp/scripts

psql -d bigfitnessgains -a -f populate_tables.sql
```

Inspect DB via the shell
```
psql -d bigfitnessgains
bigfitnessgains=# \?
bigfitnessgains=# \dt main*
 public | mainapp_exercise              | table | rcstats
 public | mainapp_exercisetomusclegroup | table | rcstats
 public | mainapp_musclegroup           | table | rcstats
 public | mainapp_workout               | table | rcstats
 public | mainapp_workoutset            | table | rcstats

```


#### Start the dev server
```
python manage.py syncdb
# The first time through you will need to create an superuser for the admin

python manage.py migrate
heroku run python manage.py check_permissions

python manage.py runserver_plus
```

**EXPECTED RESULT:** 
* You can now connect to the landing page http://127.0.0.1:8000
* You can now connect to the admin page http://127.0.0.1:8000/admin/
* You should see the output in the terminal running 'runserver_plus'
```
Validating models...
0 errors found

Django version 1.5.7, using settings 'bigfitnessgains.settings.dev'
Development server is running at http://127.0.0.1:8000/
Using the Werkzeug debugger (http://werkzeug.pocoo.org/)
Quit the server with CONTROL-C.
 * Running on http://127.0.0.1:8000/
 * Restarting with reloader
Validating models...
0 errors found

Django version 1.5.7, using settings 'bigfitnessgains.settings.dev'
Development server is running at http://127.0.0.1:8000/
Using the Werkzeug debugger (http://werkzeug.pocoo.org/)
Quit the server with CONTROL-C.

127.0.0.1 - - [01/May/2014 18:44:28] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [01/May/2014 18:44:29] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [01/May/2014 18:44:29] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [01/May/2014 18:44:34] "GET /admin HTTP/1.1" 301 -
```



Migrations

If you have an old version of the app, you'll need to migrate your database schema to the latest version.
Per south documentation:
```
python manage.py schemamigration mainapp --auto
```

Developement Guide
===========

### Developing Statics
*DO NOT* Modify the bootstrap files manually, use a new custom file to hold the changes.
* All work should be done in assets/css, assets/js, etc.
* django-compressor should automaticall compress the resource to bigfitnessgains/static/CACHE assuming you have marked the resource in the template Example:
** bigfitnessgains/static is ignored by git
** TODO not sure if this is desired or not.
```
{% load compress %}
    {% compress css %}
    <link href="{{ STATIC_URL }}css/custom-styles.css" rel="stylesheet" media="all">
    {% endcompress %}
```

Deployment Guide
===========
http://bigfitnessgains.herokuapp.com/

**IMPORTANT** - *'heroku run python manage.py compress'* is important, so that the static resources are sent to AWS and a manifest is generated. For some reason this is not done during Heroku's compression step.
```
git push heroku master
heroku run python manage.py compress
heroku run python manage.py syncdb
heroku run python manage.py migrate
heroku run python manage.py check_permissions
```

Testing Guide
============
Tests for the main app are located in the /bigfitnessgains/apps/mainapp/tests folder, split out based on functionality.

To run tests, from the command line:
```
python manage.py test bigfitnessgains.apps.mainapp.test
```

