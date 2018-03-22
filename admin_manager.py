from admin import create_core
from flask_script import Manager, Server
from gevent import wsgi, monkey

monkey.patch_all()

core = create_core('default')
app = core.app
manager = Manager("server", Server)

wsgi.WSGIServer(('0.0.0.0', 5000), app).serve_forever()

