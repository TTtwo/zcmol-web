from flask_restful import Api
from ..controller import CustomController
from .daily import *

daily_controller = CustomController(import_name=__name__, name='client-daily',
                                    prefix='/api')


api = Api(daily_controller.blueprint)
api.add_resource(Daily, '/<int:daily_id>/daily')
