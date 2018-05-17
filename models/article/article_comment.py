from kernel.database import DB
from ...models.utils.mixin import CommentMixin
from ...models.utils.mixin import HiddenMixin
from ...models.utils.mixin import ModelMixin
from ...models.article.article import Article


class ArticleComment(DB.Model, ModelMixin, HiddenMixin, CommentMixin):
    __tablename__ = 'article_comment'

    id = DB.Column(DB.Integer, primaryKey=True, autoincrement=True)
    article_id = DB.Column(DB.Integer, DB.foreignKey(Article.id))
    article_comment_id = DB.Column(DB.Integer, DB.foreignKey(id), nullable=True)
