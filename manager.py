from flask_script import Manager, Server
from app import create_core
from models import create_all


core = create_core('default')
app = core.app
manager = Manager(app)
manager.add_command("server", Server)


@manager.command
def create():
   create_all()


if __name__ == '__main__':
    manager.run(default_command="server")
