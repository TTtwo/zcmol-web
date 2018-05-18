from flask_script import Manager
from flask_script import Server
from app.client import create_core
from app.models import Model

core = create_core('default')
app = core.app
app.debug = True
manager = Manager(app)
manager.add_command("server", Server)


@manager.command
def create():
    model = Model()
    model.create_all()


if __name__ == '__main__':
    manager.run(default_command="server")
