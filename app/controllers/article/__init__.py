from app.controllers.controller import CustomController
from kernel.response import Response
from models import MODELS

article_controller = CustomController(import_name=__name__, name='article', prefix='/article')
_a = article_controller


@_a.get('/index', methods=["GET"])
def index():
    ary = MODELS["DailyArticle"].query.all()
    print(ary[0].da_id)
    r = str(ary[0])
    return r
