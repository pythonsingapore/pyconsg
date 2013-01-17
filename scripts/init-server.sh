#!/bin/bash
# This script installs dependencies on the webserver, such as pip, virtualenv,
# virtualenvwrapper and mercurial. Then it copies the website files into the
# web app folder and creates the database.

# Get some user input
DB_PASSWORD=
while [ -z $DB_PASSWORD ]
do
    echo -n 'DB Password: '
    read DB_PASSWORD
done

EMAIL_PASSWORD=
while [ -z $EMAIL_PASSWORD ]
do
    echo -n 'EMAIL Password: '
    read EMAIL_PASSWORD
done


# Define a variable
PYTHON=python2.7


# Create some folders if not present
mkdir -p ~/src
mkdir -p ~/tmp
mkdir -p ~/lib/$PYTHON


# Install pip, virtualenv, virtualenvwrapper and mercurial
easy_install-2.7 pip
pip install virtualenv

cd ~/src
wget 'http://pypi.python.org/packages/source/v/virtualenvwrapper/virtualenvwrapper-3.6.tar.gz'
tar -xzf virtualenvwrapper-3.6.tar.gz
cd virtualenvwrapper-3.6
PYTHONPATH=$HOME/lib/$PYTHON $PYTHON setup.py install --home=$HOME

pip install mercurial


# Add stuff to .bashrc
echo "export PYTHON=${PYTHON}" >> $HOME/.bashrc
echo 'export WORKON_HOME="$HOME/Envs"' >> $HOME/.bashrc
echo 'export VIRTUALENVWRAPPER_TMPDIR="$WORKON_HOME/tmp"' >> $HOME/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/$PYTHON" >> $HOME/.bashrc
echo 'source $HOME/bin/virtualenvwrapper.sh' >> $HOME/.bashrc
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> $HOME/.bashrc
echo 'export PIP_RESPECT_VIRTUALENV=true' >> $HOME/.bashrc


# Create the virtual environment
cd $HOME
source .bashrc
mkvirtualenv -p python2.7 pyconsg


# Install all packages into virtual environment
source $HOME/Envs/pyconsg/bin/activate
pip install -r ~/src/pyconsg/pyconsg/requirements.txt --upgrade
pip install psycopg2


# Delete folders created by webfaction
rm -rf ~/webapps/pyconsg_django/lib/python2.7/*
rm -rf ~/webapps/pyconsg_django/pyconsg


# Place our own folder & prepare local_settings.py
cp -rf ~/src/pyconsg/pyconsg ~/webapps/pyconsg_django
cd ~/webapps/pyconsg_django/pyconsg/pyconsg/settings/local
cp local_settings.py.sample local_settings.py
sed -i 's/DB_PASSWORD/'$DB_PASSWORD'/g' local_settings.py
sed -i 's/EMAIL_PASSWORD/'$EMAIL_PASSWORD'/g' local_settings.py

# Initialize database
cd ~/webapps/pyconsg_django/pyconsg
./manage.py syncdb --all
./manage.py migrate --fake
fab prod run_deploy_website
fab loaddata
