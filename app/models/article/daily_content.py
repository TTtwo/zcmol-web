from ...kernel.database import DB
from ..article.article import Article
from ..utils.mixin import ArticleMixin
from sqlalchemy.orm import relationship
from enum import Enum


class DailyContentType(Enum):
    MUSIC = 'music++'
    SAD = 'sad++'
    PICTURE = 'picture++'


class DailyContent(DB.Model, ArticleMixin):
    __tablename__ = 'daily_content'

    daily_type = DB.Column(DB.String(20), default=DailyContentType.MUSIC.value)
    article_id = DB.Column(DB.Integer, DB.ForeignKey(Article.id), nullable=False)
    article = relationship('Article', backref=DB.backref('daily_content', uselist=False))
