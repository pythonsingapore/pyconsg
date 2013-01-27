"""Fabric tasks for local development."""
from django.conf import settings

from fabric.api import local
from fabric.api import settings as fab_settings

from development_fabfile.fabfile.local import flake8, test as test_orig


USER_AND_HOST = '-U {0} -h localhost'.format(settings.LOCAL_PG_ADMIN_ROLE)


def create_database():
    """Creates the local database."""
    local('psql {0} -c "CREATE DATABASE {1}"'.format(
        USER_AND_HOST, settings.PROJECT_NAME))
    local('psql {0} -c "GRANT ALL PRIVILEGES ON DATABASE {1}'
          ' to {1}"'.format(USER_AND_HOST, settings.PROJECT_NAME))
    local('psql {0} {1} -c "GRANT ALL PRIVILEGES ON ALL TABLES'
          ' IN SCHEMA public TO {1}"'.format(
              USER_AND_HOST, settings.PROJECT_NAME))


def drop_database():
    """Drops the local database."""
    with fab_settings(warn_only=True):
        local('psql {0} -c "DROP DATABASE {1}"'.format(
            USER_AND_HOST, settings.PROJECT_NAME))


def test(options=None, integration=1,
         settings='pyconsg.settings.test_settings'):
    flake8()
    return test_orig(options, integration, settings)


def rebuild():
    """Deletes and re-creates the local database."""
    drop_database()
    create_database()
    local('python2.7 manage.py syncdb --noinput')
    local('python2.7 manage.py migrate')
    loaddata()


def dumpdata():
    """Dumps everything.

    Remember to add new dumpdata commands for new apps here so that you always
    get a full initial dump when running this task.

    """
    local('python2.7 ./manage.py dumpdata --indent 4 --natural auth.user > pyconsg/fixtures/bootstrap_auth.json')  # NOPEP8
    # account fixtures get created via signals when auth fixtures are loaded
    local('python2.7 ./manage.py dumpdata --indent 4 --natural sites > pyconsg/fixtures/bootstrap_sites.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural conference > pyconsg/fixtures/bootstrap_conference.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural speakers > pyconsg/fixtures/bootstrap_speakers.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural proposals > pyconsg/fixtures/bootstrap_proposals.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural cms > pyconsg/fixtures/bootstrap_cms.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural sitetree > pyconsg/fixtures/bootstrap_sitetree.json')  # NOPEP8


def loaddata():
    """Loads available fixtures."""
    local('python2.7 manage.py loaddata bootstrap_auth.json')
    local('python2.7 manage.py loaddata bootstrap_sites.json')
    local('python2.7 manage.py loaddata bootstrap_conference.json')
    local('python2.7 manage.py loaddata bootstrap_speakers.json')
    local('python2.7 manage.py loaddata bootstrap_proposals.json')
    local('python2.7 manage.py loaddata bootstrap_cms.json')
    local('python2.7 manage.py loaddata bootstrap_sitetree.json')
