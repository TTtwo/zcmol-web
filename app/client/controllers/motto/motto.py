from app.kernel.database import ModelHelper
from app.models import Model
from app.kernel.utils.response import resp_to_json
from flask_restful import Resource
from flask_sqlalchemy import Pagination
from webargs import fields
from webargs.flaskparser import use_kwargs
from flask import current_app
import json


class Motto(Resource):

    @use_kwargs({
        'page': fields.Int(min=1, required=True),
        'per_page': fields.Int(min=1, required=True)
    })
    def get(self, page, per_page):
        name = 'motto'
        key = 'motto%i' % page
        cache = current_app.core.cache
        if cache.hget(name, key):
            data = cache.hget(name, key)
            data = json.loads(data)
            return resp_to_json(data=data)
        pagination: Pagination = Model \
            .Motto \
            .query \
            .filter_by(_hidden=0) \
            .order_by(Model.Motto.id.desc()) \
            .paginate(page=page, per_page=per_page)
        motto_items = [
            ModelHelper.serialize(item)
            for item in pagination.items
        ]
        data = {
            'motto': motto_items,
            'paging': {
                'has_next': pagination.has_next,
                'has_prev': pagination.has_prev,
                'next_idx': pagination.next_num,
                'prev_idx': pagination.prev_num,
                'current_idx': pagination.page,
                'total_pages': pagination.pages
            }
        }
        cache.hset(name, key, json.dumps(data))
        cache.expire(name, 3600)
        return resp_to_json(data=data)
