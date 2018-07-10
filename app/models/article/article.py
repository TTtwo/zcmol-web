from enum import Enum
from ...kernel.database import DB
from ..utils.mixin import HiddenMixin
from ..utils.mixin import ModelMixin


class ArticleStateEnum(Enum):
    PUBLIC = 1
    PRIVATE = 2


class ArticleContentTypeEnum(Enum):
    DAILY = 1
    BLOG = 2


class Article(DB.Model, ModelMixin, HiddenMixin):
    __tablename__ = 'article'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    state = DB.Column(DB.Integer, nullable=False, default=ArticleStateEnum.PUBLIC.value)
    content_type = DB.Column(DB.Integer, nullable=False, default=ArticleContentTypeEnum.DAILY.value)
