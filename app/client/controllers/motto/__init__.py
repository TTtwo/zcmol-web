from flask_restful import Api
from ..controller import CustomController
from .motto import *

motto_controller = CustomController(import_name=__name__, name="client-motto",
                                    prefix='/api')
api = Api(motto_controller.blueprint)
api.add_resource(Motto, '/motto')
