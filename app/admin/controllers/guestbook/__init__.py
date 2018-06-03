from flask_restful import Api
from ..controller import AdminController
from .guestbook import *

guestbook_controller = AdminController(import_name=__name__, name='admin-guestbook',
                                       prefix='/admin')
api = Api(guestbook_controller.blueprint)

api.add_resource(Guestbook, '/guestbook')
api.add_resource(GuestbookDetail, '/<int:guestbook_id>/guestbook')
