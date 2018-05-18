from app.models import Model
from flask_restful import Api
from flask_restful import Resource
from app.kernel.database import DB
from ..controller import AdminController
from app.kernel.database import ModelHelper
from app.kernel.response import Response
from webargs import fields
from webargs.flaskparser import use_kwargs
from webargs import missing

link_controller = AdminController(import_name=__name__, name='admin-link',
                                  prefix='/admin')

api = Api(link_controller.blueprint)


@api.resource('/link')
class Link(Resource):

    @use_kwargs({
        'hidden': fields.Bool(missing=None)
    })
    def get(self, hidden: bool):
        filter_arg = {}
        if hidden is not None:
            filter_arg["hidden"] = hidden


        links = [
            ModelHelper.serialize(link)
            for link in links_res
        ]
        return Response.to_json(links=links)
