from ..kernel.database import DB
from .utils.mixin import CommentMixin
from .utils.mixin import ModelMixin


class GuestBook(DB.Model, ModelMixin, CommentMixin):
    __tablename__ = 'guestbook'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    my_reply = DB.Column(DB.Text, default='...')
