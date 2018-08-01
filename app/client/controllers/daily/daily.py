from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from webargs import fields
from webargs.flaskparser import use_kwargs
from app.kernel.utils.response import resp_to_json
from app.kernel.utils.response import RespError
from flask_restful import Resource
from flask_restful import request
from flask_sqlalchemy import BaseQuery
from flask import current_app
import json


class Daily(Resource):

    def get(self, daily_id: int):
        key = 'daily{}'.format(daily_id)
        cache = current_app.core.cache
        if cache.get(key):
            data = cache.get(key)
            data = json.loads(data)
            return resp_to_json(article=data)
        daily: BaseQuery = Model \
            .Article \
            .query \
            .filter_by(id=daily_id,
                       content_type=Model.ArticleContentType.DAILY.value) \
            .limit(1)
        prev: BaseQuery = Model \
            .Article \
            .query \
            .filter(Model.Article.id < daily_id) \
            .limit(1)
        next: BaseQuery = Model \
            .Article \
            .query \
            .filter(Model.Article.id > daily_id) \
            .limit(1)
        if daily.first():
            daily = ModelHelper.serialize(daily[0], daily_content=daily[0].daily_content)
            daily['prev'] = prev[0].id if prev.first() else None
            daily['next'] = next[0].id if next.first() else None
            cache.set(key, json.dumps(daily))
            cache.expire(key, 1800)

        return resp_to_json(article=daily)
