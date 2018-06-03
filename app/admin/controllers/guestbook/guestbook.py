from flask_restful import Resource

from webargs import fields
from webargs.flaskparser import use_kwargs

from app.models import Model
from app.kernel.database import ModelHelper
from app.kernel.database import DB
from app.kernel.utils.response import *

from datetime import datetime


class Guestbook(Resource):

    @use_kwargs({})
    def get(self):
        query: list[Model.GuestBook] = Model.GuestBook.query.all()
        items = [
            ModelHelper.serialize(item)
            for item in query
        ]
        return resp_to_json(items=items)


class GuestbookDetail(Resource):

    @use_kwargs({
        'my_reply': fields.Str(max=512, required=True)
    })
    def patch(self, guestbook_id, my_reply):
        guestbook: Model.GuestBook = Model.GuestBook.query.get(guestbook_id)
        if guestbook is None:
            return 'guestbook_id {} is not exist'.format(guestbook_id)
        guestbook.my_reply = my_reply
        DB.session.commit()
        return 201
