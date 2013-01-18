PyCon SG 2013 Website Deployment
================================

This document describes how to deploy the PyCon SG 2013 Website on a new
Webfaction server.

You need to be able to SSH into the server, so you should use either OSX or
Ubuntu. Ubuntu can be installed into a VirtualBox for free.

Please note that this document only describes the process of the initial
deployment. If you want to contribute to the project and deploy later versions
please refer to the development documentation.

Buying the server
-----------------

In order to buy a new server, visit https://www.webfaction.com/signup/
and fill out the form.

* Chose a short username, such as ``pyconsg``.
* Chose ``Singapore`` as ``Server location``
* Leave the ``Domain`` field empty
* Chose ``Django`` as ``Software``

After signing up you will receive a confirmation email. After less than one
hour you will receive a second email with your login details.


Configuring the server via Control Panel
----------------------------------------

Once you have the confirmation email, login to your account at
https://my.webfaction.com/.

.. note::

    In the following instructions, please replace ``username`` with the
    username of your Webfaction account.

**Change the panel password**::

    https://my.webfaction.com/change_password/create

**Change the SSH password**::

    https://my.webfaction.com/change_ssh_password/create

**Delete any existing applications**

When you bought the server and indicated which software you want to use,
Webfaction usually creates that software for you. However, we want to create
it with a different name, so you can delete any existing applications.

**Create new Django application**::

    https://my.webfaction.com/applications
    Name: pyconsg_django
    App Category: Django
    App Type: Django (latest version) (mod_wsgi 3.3 / Python 2.7)

**Create new Static application**::

    https://my.webfaction.com/applications
    Name: pyconsg_static
    App Category: Static
    App Type: Static only (no .htaccess)
    Extra info: expires max

**Create new Media application**::

    https://my.webfaction.com/applications
    Name: pyconsg_media
    App Category: Static
    App Type: Static only (no .htaccess)
    Extra info: expires max

**Delete any existing sites**

Webfaction will create a site for the app it has created automatically. Since
we have deleted that app in a previous step, we can also delete that site.

**Create PyCon SG Website**::

    https://my.webfaction.com/websites
    Name: pyconsg
    Security: https
    Subdomains: username.webfactional.com
    App1: pyconsg_django with URL: /
    App2: pyconsg_static with URL: /static/
    App3: pyconsg_media with URL: /media/

**Create Mailbox**::

    https://my.webfaction.com/mailboxes
    # Click at the existing mailbox
    # Chose a password and note it down

**Create Database**::

    https://my.webfaction.com/databases
    Name: pyconsg
    Type: PostgreSQL
    Username: pyconsg
    # Enter a password and note it down

At this point you should be able to visit https://username.webfactional.com
and see a vanilla Django welcome page.


Deploying the repository on the server
--------------------------------------

Now you need to SSH into the server, clone the website and execute an intial
deployment script. The script will copy the files into the correct folder and
load some fixtures into the database::

    ssh pyconsg@pyconsg.webfactional.com
    mkdir -p ~/src && cd ~/src
    git clone git://github.com/pythonsingapore/pyconsg.git
    cd pyconsg/scripts
    ./init-server.sh
    # Enter the DB password
    # Enter the email password


Change Apache settings
----------------------

When Webfaction sets up the Apache webserver it assumes that the project is
names `myproject` but in our case it is named `pyconsg`. Therefore we need
to change some paths in the `httpd.conf` file::

    vim ~/webapps/pyconsg_django/apache2/conf/httpd.conf

Make sure that the wsgi part of the config looks like this::

    WSGIDaemonProcess pyconsg_django processes=2 threads=12 python-path=/home/pyconsg/webapps/pyconsg_django:/home/pyconsg/webapps/pyconsg_django/pyconsg:/home/pyconsg/Envs/pyconsg/lib/python2.7/site-packages
    WSGIProcessGroup pyconsg_django
    WSGIRestrictEmbedded On
    WSGILazyInitialization On
    WSGIScriptAlias / /home/pyconsg/webapps/pyconsg_django/pyconsg/pyconsg/wsgi.py

After changing the config, restart apache like so::

    ~/webapps/pyconsg_django/apache2/bin/restart

At this point you should be able to visit https://username.webfactional.com
and see the PyCon SG website, setup with some fixtures as test data.


Setup cronjobs
--------------

TODO


Import database
---------------

TODO


Import media files
------------------

TODO
