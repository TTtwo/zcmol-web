from flask_script import Manager, Server
from kernel.core import app
from models import create_all


manager = Manager(app)
manager.add_command("server", Server)

@manager.command
def create():
   create_all()

if __name__ == '__main__':
    manager.run()
