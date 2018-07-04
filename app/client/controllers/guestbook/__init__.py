from flask_restful import Api
from ..controller import CustomController
from .guestbook import *

guestbook_controller = CustomController(import_name=__name__, name='client-guestbook',
                                        prefix='/api')

api = Api(guestbook_controller.blueprint)
api.add_resource(Guestbook, '/guestbook')
