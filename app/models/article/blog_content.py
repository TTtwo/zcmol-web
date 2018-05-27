from ...kernel.database import DB
from ..article.article import Article
from ..utils.mixin import ModelMixin
from ..utils.mixin import HiddenMixin
from ..utils.mixin import ArticleMixin
from sqlalchemy.orm import relationship

class BlogContentCategory(DB.Model, ModelMixin, HiddenMixin):
    __tablename__ = 'blog_content_category'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    category_name = DB.Column(DB.String(50), nullable=False, unique=True)


class BlogTag(DB.Model, ModelMixin, HiddenMixin):
    __tablename__ = 'blog_tag'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    tag_name = DB.Column(DB.String(20), nullable=False, unique=True)


class BlogContent(DB.Model, ArticleMixin):
    __tablename__ = 'blog_content'

    content_category_id = DB.Column(DB.Integer,
                                    DB.ForeignKey(BlogContentCategory.id),
                                    nullable=False)
    tag_id = DB.Column(DB.Integer, DB.ForeignKey(BlogTag.id), nullable=False)
    article_id = DB.Column(DB.Integer, DB.ForeignKey(Article.id), nullable=False)
    article = relationship('article', backref=DB.backref('blogContent'))
