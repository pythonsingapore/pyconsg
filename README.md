PyCon Singapore 2013
====================

This Django project is the PyCon Singapore 2013 website.

Quick Start on OS X
--------------------

Before proceeding with the setup guide, make sure you have the following packages installed.

* [PostgreSQL 9.2](http://www.postgresql.org/download/macosx/)
* [virtualenv](http://pypi.python.org/pypi/virtualenv)
* [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper)

If you use [MacPorts](http://www.macports.org/install.php), you can execute following command to install all the packages above.

```sh
sudo port install postgresql92 postgresql92-server virtualenv virtualenvwrapper
```

Please refer to the troubleshooting section if you are new to any of the above packages.

Local Setup
-----------

Clone this project.

```sh
mkdir -p ~/Projects/pyconsg/
cd ~/Projects/pyconsg/
git clone git://github.com/pythonsingapore/pyconsg.git pyconsg
```

Create a virtualenv and install project dependencies.

```sh
mkvirtualenv -p python2.7 pyconsg
cd ~/Projects/pyconsg/pyconsg/
pip install -r requirements.txt
```

Create your `local_settings.py` and make your changes.

```sh
cd ~/Project/pyconsg/pyconsg/pyconsg/settings/local
cp local_settings.py.sample local_settings.py
vim local_settings.py
```

Most values should have good defaults and you should basically just change your name and email for the ADMINS setting.

Create the default user for database access.

```sh
createuser pyconsg -U postgres -dslrP
```

When prompted for password use `pyconsg`.

Initialize your local database with sample data.

```sh
cd ~/Projects/pyconsg/pyconsg/
fab rebuild
```

Running the Server Locally
--------------------------

```sh
workon pyconsg
cd ~/Projects/pyconsg/pyconsg/
./manage.py runserver
```

Troubleshooting
---------------

### psycopg2.OperationalError: could not connect to server: Permission denied

Edit your `~/.bash_profile` to include the following line.

```sh
export PGHOST=localhost
```

### New to PostgreSQL

Assuming you have just installed PostgreSQL using MacPorts, you need to configure a default database.

```sh
sudo mkdir -p /opt/local/var/db/postgresql92/defaultdb
sudo chown postgres:postgres /opt/local/var/db/postgresql92/defaultdb
sudo su postgres -c '/opt/local/lib/postgresql92/bin/initdb -D /opt/local/var/db/postgresql92/defaultdb'
```

To start the PostgreSQL server.

```sh
sudo su postgres -c '/opt/local/lib/postgresql92/bin/pg_ctl start -D /opt/local/var/db/postgresql92/defaultdb'
```

As this is a very long command, you may wish to configure your PostgreSQL service to start automatically with your system.

```sh
sudo su postgres -c '/opt/local/lib/postgresql92/bin/pg_ctl start -D /opt/local/var/db/postgresql92/defaultdb'
```

### New to virtualenv and virtualenvwrapper

Assuming you have just installed virtualenv and virtualenvwrapper using MacPorts, you need to edit your `~/.bash_profile` to include the following line.

```sh
source /opt/local/bin/virtualenvwrapper.sh-2.7
```
