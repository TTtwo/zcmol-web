from ...kernel.database import DB
from ..article.article import Article
from ..utils.mixin import ArticleMixin


class DailyContent(DB.Model, ArticleMixin):
    __tablename__ = 'daily_content'

    article_id = DB.Column(DB.Integer, DB.ForeignKey(Article.id))
