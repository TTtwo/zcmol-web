from flask_script import Manager, Server
# from zcmol.models import create_all
from zcmol.kernel.core import app

manager = Manager(app)
manager.add_command("server", Server())

@manager.command
def hello():
    print('how are you')

# @manager.command
# def create():
#    create_all()
#
if __name__ == '__main__':
    manager.run()
