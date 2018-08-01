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
        article: BaseQuery = Model.Article.query.get(daily_id)
        comments = article.article_comment if article else []
        comments = [
            ModelHelper.serialize(item)
            for item in comments
        ]
        return resp_to_json(comments=comments)

    @use_kwargs({
        'nickname': fields.Str(max=32, required=True),
        'content': fields.Str(max=512, required=True),
        'email': fields.Str(max=32),
        'website': fields.Str(max=512),
        'reply_id': fields.Int(missing=None)
    })
    def post(self, daily_id, nickname, content, email, website, reply_id):
        cache = current_app.core.cache
        ip = request.headers['X-Forwarded-For']
        if cache.get(ip.strip()):
            return resp_to_json(error=RespError.FRE_COMMENT.value)
        cache.set(ip.strip(), 1, px=30)
        article: Model.Article = Model.Article.query.get(daily_id)
        comment = Model.ArticleComment(nickname=nickname,
                                       content=content,
                                       email=email,
                                       website=website,
                                       article_comment_id=reply_id)
        comment.article = article
        DB.session.add(comment)
        DB.session.commit()
        return resp_to_json(data='增加成功~~')
