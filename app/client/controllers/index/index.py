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
        # 获取前50条Guestbook
        guestbooks: BaseQuery = Model \
            .GuestBook \
            .query \
            .order_by(Model.GuestBook.id.desc()) \
            .limit(50) \
            .all()
        # 获取daily article
        dailys: BaseQuery = Model \
            .DailyContent \
            .query \
            .order_by(Model.DailyContent.id.desc()) \
            .limit(13)
        # 整合数据
        link_items = [
            ModelHelper.serialize(item)
            for item in links
        ]
        guestbook_items = [
            ModelHelper.serialize(item)
            for item in guestbooks
        ]
        daily_items = [
            ModelHelper.serialize(item, article=item.article)
            for item in dailys
        ]
        data = {
            'links': link_items,
            'guestbooks': guestbook_items,
            'dailys': daily_items
        }
        return resp_to_json(data=data)
