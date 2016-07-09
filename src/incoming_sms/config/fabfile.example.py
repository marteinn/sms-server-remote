from fabric.state import env
from fabric.decorators import task
from fabric.api import run


@task
def prod():
    env.host_string = 'XX.XX.XX.XX'
    env.user = 'root'
    env.password = 'example password'


@task
def restart_apache():
    run('service apache restart')
