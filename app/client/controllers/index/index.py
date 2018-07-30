from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from app.kernel.utils.response import resp_to_json
from flask_restful import Resource
from flask_sqlalchemy import BaseQuery
from flask import current_app
import json


class Index(Resource):
    def get(self):
        key = name = 'index'
        cache = current_app.core.cache
        if cache.hget(name, key):
            data = cache.hget(name, key)
            data = json.loads(data)
            return resp_to_json(data=data)
        # 获取所有links
        links: BaseQuery = Model \
            .Link \
            .query \
            .filter_by(_hidden=False) \
            .all()
        # 获取前30条Guestbook
        guestbooks: BaseQuery = Model \
            .GuestBook \
            .query \
            .order_by(Model.GuestBook.id.desc()) \
            .limit(30) \
            .all()
        # 获取daily article
        daily: BaseQuery = Model \
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
            ModelHelper.filter(
                ModelHelper.serialize(item, article=item.article),
                ['content'])
            for item in daily
        ]
        data = {
            'links': link_items,
            'guestbooks': guestbook_items,
            'daily': daily_items
        }
        cache.hset(name, key, json.dumps(data))
        cache.expire(name, 3600 * 24)
        return resp_to_json(data=data)
