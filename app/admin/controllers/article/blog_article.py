from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models.article.article import ArticleContentTypeEnum
from app.models.article.article import ArticleStateEnum
from app.models import Model
from app.kernel.utils.response import resp_to_json

from datetime import datetime

from webargs import fields
from marshmallow import validate
from webargs.flaskparser import use_kwargs

from flask_restful import Resource
from flask_sqlalchemy import BaseQuery

STATE = [v.value
         for v in ArticleStateEnum.__members__.values()]


class BlogArticle(Resource):
    @use_kwargs({
        "hidden": fields.Bool(missing=False)
    })
    def get(self, hidden):
        filter_args = {
            '_hidden': hidden,
            'content_type': ArticleContentTypeEnum.BLOG.value
        }
        query: BaseQuery = DB.session \
            .query(Model.Article) \
            .filter_by(**filter_args) \
            .join(Model.Article.blog_content) \
            .all()
        items = [
            ModelHelper.serialize(item, contents={
                'title': item.blog_content.title
            })
            for item in query
        ]
        print(items)
        return resp_to_json(items=items)

    @use_kwargs({
        'title': fields.Str(max=20),
        'content': fields.Str(),
        'hidden': fields.Bool(),
        'tag_ids': fields.List(fields.Int(), required=True),
        'category': fields.Int(required=True)
    })
    def post(self, title, content, tag_ids, category, state, hidden):
        pass
