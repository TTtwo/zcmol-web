from flask_restful import Api
from ..controller import CustomController
from .index import *

index_controller = CustomController(import_name=__name__, name='client-index',
                                    prefix='/api')
api = Api(index_controller.blueprint)

api.add_resource(Index, '/index')
