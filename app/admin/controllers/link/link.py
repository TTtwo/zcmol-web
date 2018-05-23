from flask_restful import Resource

from webargs import fields
from webargs.flaskparser import use_kwargs

from app.models import Model
from app.kernel.database import ModelHelper
from app.kernel.database import DB
from app.kernel.utils.response import *

from datetime import datetime


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
        return resp_to_json(links=links)

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
    def patch(self, link_id: int, name: str, url: str, img: str, desc: str, hidden: bool):
        query: Model.Link = Model.Link.query.get(link_id)
        if query is None:
            return 'link_id {} is not exists'.format(link_id)
        if name:
            query.name = name
        if url:
            query.url = url
        if img:
            query.img = img
        if desc:
            query.desc = desc
        if hidden:
            query.hidden = hidden

        query.change_at = datetime.now()
        DB.session.commit()
        query: Model.Link = Model.Link.query.get(link_id)
        return resp_to_json(ModelHelper.serialize(query))
