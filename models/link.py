from kernel.database import DB
from ..models.utils.mixin import ModelMixin
from ..models.utils.mixin import HiddenMixin


class Link(DB.Model, ModelMixin, HiddenMixin):
    __tablename__ = 'links'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String(30), nullable=False)
    url = DB.Column(DB.String(150), nullable=False)
    img = DB.Column(DB.String(150), default="")
    desc = DB.Column(DB.String(150), default="")
