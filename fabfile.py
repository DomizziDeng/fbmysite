from fabric.api import local

def prepare_deploy():
    local("./manage.py test ip")
    local("git add -p && git commit")
    local("git push")
