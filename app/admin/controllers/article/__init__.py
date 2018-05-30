from flask_restful import Api
from ..controller import AdminController
from .daily_article import *
from .blog_article import *

article_controller = AdminController(import_name=__name__, name="admin-article",
                                     prefix="/admin")
api = Api(article_controller.blueprint)

api.add_resource(DailyArticle, '/daily_article')
api.add_resource(DailyArticleDetail, '/<int:article_id>/daily_article')
api.add_resource(BlogArticle, '/blog_article')
