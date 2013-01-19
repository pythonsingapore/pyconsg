#!/bin/bash
source $HOME/bin/script-settings-pyconsg.sh
source $HOME/Envs/$VENV_NAME/bin/activate

$HOME/webapps/$DJANGO_APP_NAME/$PROJECTNAME/manage.py retry_deferred
