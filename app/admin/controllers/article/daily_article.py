from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models.article.article import ArticleContentTypeEnum
from app.models.article.article import ArticleStateEnum
from app.models.article.daily_content import DailyContentType
from app.models import Model
from app.kernel.utils.response import resp_to_json

from datetime import datetime

from webargs import fields
from marshmallow import validate
from webargs.flaskparser import use_kwargs

from flask_restful import Resource
from flask_sqlalchemy import BaseQuery

# CONTENT_TYPES = [v.value
#                  for v in ArticleContentTypeEnum.__members__.values()]
STATE = [v.value
         for v in ArticleStateEnum.__members__.values()]
DAILY_CONTENT_TYPES = [v.value
                       for v in DailyContentType.__members__.values()]


class DailyArticle(Resource):

    @use_kwargs({
        # 'content_type': fields.Int(required=True,
        #                            validate=validate.OneOf(CONTENT_TYPES))
        # 'state': fields.Int(required=True,
        #                     validate=validate.OneOf(ARTICLE_STATE)) })`
        'hidden': fields.Bool(missing=False)
    })
    def get(self, hidden):
        filter_arg = {
            "_hidden": hidden,
            'content_type': ArticleContentTypeEnum.DAILY.value
        }
        query: BaseQuery = DB.session \
            .query(Model.Article) \
            .filter_by(**filter_arg) \
            .join(Model.Article.daily_content) \
            .all()
        items = [
            ModelHelper.serialize(item, contents={
                'title': item.daily_content.title,
                'daily_type': item.daily_content.type
            })
            for item in query
        ]
        return resp_to_json(items=items)

    @use_kwargs({
        'title': fields.Str(max=32, required=True),
        'content': fields.Str(required=True),
        'daily_type': fields.Str(required=True,
                                 validate=validate.OneOf(DAILY_CONTENT_TYPES)),
        'state': fields.Int(required=True,
                            validate=validate.OneOf(STATE)),
        'hidden': fields.Bool(missing=False)
    })
    def post(self, title, content, daily_type, state, hidden):
        article = Model.Article(state=state,
                                _hidden=hidden,
                                content_type=ArticleContentTypeEnum.DAILY.value)
        article.daily_content = Model.DailyContent(title=title,
                                                   content=content,
                                                   daily_type=daily_type)
        DB.session.add(article)
        DB.session.commit()
        return 201


class DailyArticleDetail(Resource):
    @use_kwargs({
        'title': fields.Str(max=20),
        'content': fields.Str(),
        'hidden': fields.Bool(missing=False),
        'daily_type': fields.Str(validate=validate.OneOf(DAILY_CONTENT_TYPES))
    })
    def patch(self, article_id, title, content, hidden, daily_type):
        article: Model.Article = Model.Article.query.get(article_id)
        article._hidden = hidden
        if article is None:
            return 'article_id {} is not exists'.format(article_id)
        if title:
            article.daily_content.title = title
        if content:
            article.daily_content.content = content
        if daily_type:
            article.daily_content.daily_content = daily_type
        article.change_at = datetime.now()
        DB.session.commit()
        return 201
