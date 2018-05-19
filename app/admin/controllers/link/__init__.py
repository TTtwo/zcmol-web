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


class Links(Resource):

    @use_kwargs({
        'hidden': fields.Bool(missing=None)
    })
    def get(self, hidden: bool):
        filter_arg = {}
        if hidden is not None:
            filter_arg["_hidden"] = hidden
        links_res = Model.Link.query.filter_by(**filter_arg).all()
        links = [
            ModelHelper.serialize(link)
            for link in links_res
        ]
        return Response.to_json(links=links)

    @use_kwargs({
        'name': fields.Str(required=True, max=32),
        'url': fields.Str(required=True, max=256),
        'img': fields.Str(max=256),
        'desc': fields.Str()
    })
    def post(self, name: str, url: str, img: str, desc: str):
        params = {
            'name': name,
            'url': url
        }
        if img:
            params['img'] = img
        if desc:
            params['desc'] = desc
        link = Model.Link(**params)
        DB.session.add(link)
        DB.session.commit()
        return 201


class LinksDetail(Resource):

    @use_kwargs({
        'name': fields.Str(max=32),
        'url': fields.Str(max=256),
        'img': fields.Str(max=256),
        'desc': fields.Str(),
        'hidden': fields.Bool()
    })
    def patch(self, name: str, url: str, img: str, desc: str, hidden: bool):
        # TODO
        pass
