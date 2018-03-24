from admin import create_core
from flask_script import Manager, Server
from gevent import wsgi, monkey

monkey.patch_all()

core = create_core('default')
app = core.app
manager = Manager(app)

@manager.command
def runserver():
    wsgi.WSGIServer(('0.0.0.0', 5000), app).serve_forever()


if __name__ == '__main__':
    manager.run(default_command='runserver')




