from app.kernel.database import DB
from .utils.mixin import ModelMixin
from .utils.mixin import HiddenMixin


class Motto(DB.Model, ModelMixin, HiddenMixin):
    __tablename__ = 'motto'
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    content = DB.Column(DB.String(500), nullable=False)
    author = DB.Column(DB.String(50), nullable=False)
