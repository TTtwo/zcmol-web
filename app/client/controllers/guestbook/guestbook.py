from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from flask_sqlalchemy import Pagination
from webargs import fields
from webargs.flaskparser import use_kwargs
from app.kernel.utils.response import resp_to_json
from app.kernel.utils.response import RespError
from flask_restful import Resource
from flask_restful import request
from flask import current_app


class EmailValidate:
    @staticmethod
    def validate_email(email):
        pass


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

    @use_kwargs({
        'nickname': fields.Str(max=32, required=True),
        'content': fields.Str(max=512, required=True),
        'email': fields.Str(max=32),
        'website': fields.Str(max=512)
    })
    def post(self, nickname, content, email, website):
        cache = current_app.core.cache
        ip = request.headers['X-Forwarded-For']
        ip = "".join(ip.strip().split('.'))
        if cache.get(ip):
            return resp_to_json(error=RespError.FRE_COMMENT.value[0])
        cache.set(ip, '1', ex=30)
        gk = Model.GuestBook(nickname=nickname,
                             content=content,
                             email=email,
                             website=website)
        DB.session.add(gk)
        DB.session.commit()
        return resp_to_json(data='增加成功~')
