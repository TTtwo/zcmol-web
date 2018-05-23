from ..controller import AdminController
from flask_restful import Api
from .link import *

link_controller = AdminController(import_name=__name__, name='admin-link',
                                  prefix='/admin')

api = Api(link_controller.blueprint)

api.add_resource(Links, '/links')
api.add_resource(LinksDetail, '/<int:link_id>/link')
