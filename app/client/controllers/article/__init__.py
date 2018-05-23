from typing import List
from app.models import Model
from app.kernel.database import ModelHelper
from app.client.controllers.controller import CustomController
from app.kernel.utils.response import *

article_controller = CustomController(import_name=__name__, name='custom-article', prefix='/article')
_a = article_controller


@_a.get('/index', methods=["GET"])
def index():
    ary: List[Model.Link] = Model.Link.query.all()
    d = [
        ModelHelper.serialize(l)
        for l in ary
    ]
    return resp_to_json(item=d)
