from fabric.context_managers import lcd
from fabric.operations import local

def test():
    with lcd('backendfiddle'):
        local('py.test fiddles/test.py')
def ddocker(project='djangoname0'):
    with lcd("backendfiddle/media/djangoname0"):
        cmd = ["docker run"]
        cmd.append("--name "+project)
        cmd.append('-v "$PWD":/usr/src/app')
        cmd.append('-w /usr/src/app')
        cmd.append('-p 8000:8000')
        cmd.append('-d django')
        cmd.append('bash -c "python manage.py runserver 0.0.0.0:8000"')
        local(' '.join(cmd))