from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from flask_sqlalchemy import Pagination
from webargs import fields
from webargs.flaskparser import use_kwargs
from app.kernel.utils.response import resp_to_json
from flask_restful import Resource


class Guestbook(Resource):

    @use_kwargs({
        'page': fields.Int(min=1, required=True),
        'per_page': fields.Int(min=1, required=True)
    })
    def get(self, page, per_page):
        pagination: Pagination = Model \
            .GuestBook \
            .query \
            .order_by(Model.GuestBook.id.desc()) \
            .paginate(page=page, per_page=per_page)
        guestbook_items = [
            ModelHelper.serialize(item)
            for item in pagination.items
        ]
        data = {
            'guestbook': guestbook_items,
            'paging': {
                'has_next': pagination.has_next,
                'has_prev': pagination.has_prev,
                'next_idx': pagination.next_num,
                'prev_idx': pagination.prev_num,
                'current_idx': pagination.page,
                'total_pages': pagination.pages
            }
        }
        return resp_to_json(data=data)
