from scripts_configs.fabric.fabfile import *

from fabric.state import env

env.run_port = 1216


@task
def prod():
    env.hosts = ['alpakara.pl']
    env.user = 'alex'
    env.port = 21022
    env.project = 'smolinska'
    env.branch = env.project
    env.env = PROD
    env.code_dir = '/var/www/' + env.project
    env.repo = local('git config --get remote.origin.url', capture=True)
    env.virtualenv = "/home/{}/.virtualenvs/{}".format(env.user, env.project)
    env.dist_dir = 'build'
    env.run_env = {
        'VENV_PATH': env.virtualenv,
        'DEMO_PORT': env.run_port,
        'PROD_LOCATION': env.code_dir,
        'PROJECT_NAME': env.project,
        'WORKERS': 1,
    }

    env.domain = 'smolinska.eu'  # without www.
