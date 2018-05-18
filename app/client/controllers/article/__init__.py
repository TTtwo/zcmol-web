from typing import List
from app.client.controllers.controller import CustomController
from app.models import MODELS, Link

article_controller = CustomController(import_name=__name__, name='article', prefix='/article')
_a = article_controller


@_a.get('/index', methods=["GET"])
def index():
    ary: List[Link] = MODELS["Link"].query.all()
    ary[0].url
    print(ary)
    return 'asdsds'
