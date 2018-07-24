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
        daily: BaseQuery = Model. \
            Article. \
            query. \
            filter_by(id=daily_id). \
            one()
        if daily:
            daily = ModelHelper.serialize(daily, daily_content=daily.daily_content)
            cache.set(key, json.dumps(daily))
            cache.expire(key, 1800)

        return resp_to_json(article=daily)
