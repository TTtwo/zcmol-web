from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from app.kernel.utils.response import resp_to_json
from flask_restful import Resource
from flask_sqlalchemy import BaseQuery


class Index(Resource):
    def get(self):
        # 获取所有links
        links: BaseQuery = Model \
            .Link \
            .query \
            .filter_by(_hidden=False) \
            .all()
        # 获取前100条Guestbook
        guestbooks: BaseQuery = Model \
            .GuestBook \
            .query \
            .order_by(Model.GuestBook.id.desc()) \
            .limit(100) \
            .all()
        # 整合数据
        link_items = [
            ModelHelper.serialize(item)
            for item in links
        ]
        guestbook_items = [
            ModelHelper.serialize(item)
            for item in guestbooks
        ]
        data = {'links': link_items, 'guestbooks': guestbook_items}
        return resp_to_json(data=data)
