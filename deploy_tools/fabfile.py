from fabric.contrib.files import append, exists, sed
from fabric.api import cd, env, local, run
import random

REPO_URL = 'https://github.com/sannjka/tdd.git'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source(site_folder)
        _create_folder_structure_if_necessary()
        _update_settings(env.host)
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _create_folder_structure_if_necessary():
    for subfolder in ('database',):
        run(f'mkdir -p {subfolder}')

def _get_latest_source(site_folder):
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} {site_folder}')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'git reset --hard {current_commit}')

def _update_settings(site_name):
    setting_path = 'superlists/settings.py'
    sed(setting_path, 'DEBUG = True', 'DEBUG = False')
    sed(setting_path,
        'ALLOWED_HOSTS = .+$',
        f'ALLOWED_HOSTS = ["{site_name}"]')
    secret_key_file = 'superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(setting_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv():
    if not exists('.venv/bin/pip'):
        run(f'python3 -m venv .venv')
    run('./.venv/bin/pip install -r requirements.txt')

def _update_static_files():
    run('./.venv/bin/python manage.py collectstatic --noinput')

def _update_database():
    run('./.venv/bin/python manage.py migrate --noinput')

def _create_or_update_dotenv():
    """ Now those variables is set in settings.py
    Try to use dotenv later
    """
