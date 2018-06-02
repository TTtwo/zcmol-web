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
            ModelHelper.serialize(item,
                                  contents=item.blog_content,
                                  tags=item.blog_content.tags)
            for item in query
        ]
        return resp_to_json(items=items)

    @use_kwargs({
        'title': fields.Str(max=20, required=True),
        'content': fields.Str(required=True),
        'hidden': fields.Bool(missing=False),
        'tag_ids': fields.List(fields.Int(), reuqired=True),
        'category': fields.Int(required=True),
        'state': fields.Int(validate=validate.OneOf(STATE), missint=STATE[0])
    })
    def post(self, title, content, tag_ids, category, state, hidden):
        article = Model.Article(state=state, _hidden=hidden)
        article.blog_content = Model.BlogContent(title=title, content=content)
        article.blog_content.category = Model.BlogContentCategory \
            .query \
            .get(category)
        article.blog_content.tags = Model.BlogTag \
            .query \
            .filter(Model.BlogTag.id.in_(tag_ids)) \
            .all()
        DB.session.add(article)
        DB.session.commit()
        return 201


class BlogArticleDetail(Resource):
    @use_kwargs({
        'title': fields.Str(max=20),
        'content': fields.Str(),
        'hidden': fields.Bool(),
        'state': fields.Int(validate=validate.OneOf(STATE)),
        'category': fields.Int(),
        'tag_ids': fields.List(fields.Int())
    })
    def patch(self, article_id, title, content,
              hidden, state, category, tag_ids):
        article: Model.Article = Model.Article.query.get(article_id)
        if article is None:
            return 'blog_article_id {} is not exits'.format(article_id)
        if hidden:
            article._hidden = hidden
        if state:
            article.state = state
        if title:
            article.blog_content.title = title
        if content:
            article.blog_content.content = content
        if category:
            article.blog_content.category = category
        if tag_ids:
            blog_tag_query: list[Model.BlogTag] = Model.BlogTag \
                .query \
                .filter(Model.BlogTag.id.in_(tag_ids)) \
                .all()
            article.blog_content.tags = blog_tag_query
        article.change_at = datetime.now()
        DB.session.commit()
        return 201


class BlogTag(Resource):
    def get(self):
        query: list[Model.BlogTag] = Model.BlogTag.query.all()
        items = [
            ModelHelper.serialize(item)
            for item in query
        ]
        return resp_to_json(items=items)
