from app.controllers.controller import CustomController

article = CustomController(import_name=__name__, name='article', prefix='/article')
_a = article

@_a.get('/index')
def index():
    pass

