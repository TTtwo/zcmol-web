from ...kernel.database import DB
from ..utils.mixin import CommentMixin
from ..utils.mixin import HiddenMixin
from ..utils.mixin import ModelMixin
from ..article.article import Article

from sqlalchemy.orm import relationship


class ArticleComment(DB.Model, ModelMixin, HiddenMixin, CommentMixin):
    __tablename__ = 'article_comment'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    article_id = DB.Column(DB.Integer, DB.ForeignKey(Article.id))
    article_comment_id = DB.Column(DB.Integer, DB.ForeignKey(id), nullable=True)
    article = relationship('Article', backref=DB.backref('article_comment'))
