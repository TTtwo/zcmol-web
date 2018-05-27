from ...kernel.database import DB
from ..article.article import Article
from ..utils.mixin import ArticleMixin
from sqlalchemy.orm import relationship


class DailyContent(DB.Model, ArticleMixin):
    __tablename__ = 'daily_content'

    article_id = DB.Column(DB.Integer, DB.ForeignKey(Article.id), nullable=False)
    daily_content = relationship('DailyContent', backref=DB.backref('article'))
