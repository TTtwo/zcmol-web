from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models.article.article import ArticleContentTypeEnum
from app.models.article.article import ArticleStateEnum
from app.models import Model
from app.kernel.utils.response import resp_to_json

from webargs import fields
from marshmallow import validate
from webargs.flaskparser import use_kwargs

from flask_restful import Resource

CONTENT_TYPES = [v.value for v in ArticleContentTypeEnum.__members__.values()]


class Article(Resource):

    @use_kwargs({
        'content_type': fields.Int(required=True,
                                   validate=validate.OneOf(CONTENT_TYPES))
        # 'state': fields.Int(required=True,
        #                     validate=validate.OneOf(ARTICLE_STATE)) })`
    })
    def get(self, content_type: int):
        filter_arg = {"_hidden": False, 'content_type': content_type}
        # articles: Model.Article = Model.Article \
        #     .query \
        #     .filter_by(**filter_arg) \
        #     .all()
        # items = [
        #     ModelHelper.serialize(article)
        #     for article in articles
        # ]
        articles = DB.session.query(Model.Article, Model.DailyContent).all()
        items = [
            ModelHelper.serialize(article)
            for article in articles
        ]
        return resp_to_json(items=items)
