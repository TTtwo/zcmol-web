from app.models import Model
from app.kernel.database import DB
from flask_restful import Api
from flask_restful import Resource
from ..controller import AdminController

article_controller = AdminController(import_name=__name__, name="admin-article",
                                     prefix="/admin")
api = Api(article_controller.blueprint)


@api.resource('/article')
class Article(Resource):

    def get(self):
        links = Model.Link.query.all()
        print(len(links))
        return {'hello': 'world'}

    def post(self):
        link = Model.Link(name='123', url='123123')
        DB.session.add(link)
        DB.session.commit()
        return {'hello': 'gun'}

    def patch(self):
        return {'hello': 'patch'}
