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


class DailyComment(Resource):

    def get(self, daily_id):
        comment: BaseQuery = Model. \
            Article. \
            query. \
            filter_by(id=daily_id). \
            one(). \
            article_comment
        comment = [
            ModelHelper.serialize(item)
            for item in comment
        ]
        return resp_to_json(comments=comment)
