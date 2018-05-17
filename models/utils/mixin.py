import datetime
from kernel.database import DB


class HiddenMixin:
    _hidden = DB.Column(DB.Boolean, nullable=False,
                        default='False')

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, val: bool):
        self._hidden = val


class ModelMixin:
    create_at = DB.Column(DB.DateTime, nullable=False,
                          default=datetime.datetime.now)
    change_at = DB.Column(DB.DateTime, default=datetime.datetime.now)


class ArticleMixin:
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    title = DB.Column(DB.String(50), nullable=False)
    content = DB.Column(DB.Text, nullable=False)


class CommentMixin:
    email = DB.Column(DB.String(50))
    website = DB.Column(DB.String(120))
    content = DB.Column(DB.Text, nullable=False)
    nickname = DB.Column(DB.String(50), nullable=False)
