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
    blog_content_tag = relationship('BlogContent', secondary='blog_tag_middle_table')


class BlogContent(DB.Model, ArticleMixin):
    __tablename__ = 'blog_content'

    content_category_id = DB.Column(DB.Integer,
                                    DB.ForeignKey(BlogContentCategory.id),
                                    nullable=False)
    article_id = DB.Column(DB.Integer, DB.ForeignKey(Article.id), nullable=False)
    article = relationship('Article', backref=DB.backref('blog_content', uselist=True))
    tags = relationship('BlogTag', secondary='blog_tag_middle_table')
    category = relationship('BlogContentCategory', backref=DB.backref('blog', uselist=True))


class BlogTagMiddleTable(DB.Model):
    __tablename__ = 'blog_tag_middle_table'
    blog_id = DB.Column(DB.Integer, DB.ForeignKey(BlogContent.id),
                        nullable=True, primary_key=True)
    tag_id = DB.Column(DB.Integer, DB.ForeignKey(BlogTag.id),
                       nullable=True, primary_key=True)

