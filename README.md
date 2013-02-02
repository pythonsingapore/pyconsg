PyCon Singapore 2013
====================

This Django project is the PyCon Singapore 2013 website.

Local setup
-----------

Clone this project:

```sh
mkdir -p ~/Projects/pyconsg/
cd ~/Projects/pyconsg/
git clone git://github.com/pythonsingapore/pyconsg.git pyconsg
```

Create a virtualenv:

```sh
mkvirtualenv -p python2.7 pyconsg
cd ~/Projects/pyconsg/pyconsg/
pip install -r requirements.txt
```

Create your `local_settings.py`:

```sh
cd ~/Project/pyconsg/pyconsg/pyconsg/settings/local
cp local_settings.py.sample local_settings.py
vim local_settings.py
```

Make your changes. Most values should have good defaults and you should
basically just change your name and email for the ADMINS setting.

Create the default user for database access.

```sh
createuser pyconsg -U postgres -dslrP
```

When prompted for password use `pyconsg`

Initialize your local database with test data:

```sh
cd ~/Projects/pyconsg/pyconsg/
fab rebuild
```

Running the server locally
--------------------------

```sh
./manage.py runserver
```

Troubleshotting
---------------

### psycopg2.OperationalError: could not connect to server: Permission denied

Add the following line to your `~/.bash_profile`

```sh
export PGHOST=localhost
```