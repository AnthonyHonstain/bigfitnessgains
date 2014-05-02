BigFitnessGains
===========
Django webapp for tracking workout goals.

Initial Setup
===========

Get virtualenv, create an environment to work in, and activate your terminal.
```
sudo apt-get install python-virtualenv
virtualenv workout_env
cd workout_env/
workout_env$ source bin/activate
```
NOTE - you need to run this command every time you have a new terminal you want to work with the project:
```
cd workout_env/
source bin/active
```

Install Required Dependencies
```
sudo apt-get install python-dev build-essential libpq-dev libevent-dev libmemcached-dev postgresql-client node-less
```

Git - lets go ahead and auto rebase
```
git config branch.autosetuprebase always
```

Setup the DB to run locally (run from the django directory that contains manage.py).
```
python manage.py syncdb
# The first time through you will need to create an superuser for the admin

python manage.py migrate

python manage.py runserver_plus
```

You can now connect to the admin page! http://127.0.0.1:8000/admin/
* You should see the output in the terminal running 'runserver_plus'
* ```
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