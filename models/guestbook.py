from kernel.database import DB
from ..models.utils.mixin import CommentMixin
from ..models.utils.mixin import ModelMixin


class GuestBook(DB.Model, ModelMixin, CommentMixin):
    __tablename__ = 'guestbook'

    id = DB.Column(DB.Integer, primaryKey=True, autoincrement=True)
    my_reply = DB.Column(DB.Text, default='...')
