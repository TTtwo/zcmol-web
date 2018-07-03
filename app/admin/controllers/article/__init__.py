from flask_restful import Api
from ..controller import AdminController
from .daily_article import *
from .blog_article import *
from .blog_tag import *
from .blog_category import *

article_controller = AdminController(import_name=__name__, name="admin-index",
                                     prefix="/admin")
api = Api(article_controller.blueprint)

api.add_resource(DailyArticle, '/daily_article')
api.add_resource(DailyArticleDetail, '/<int:article_id>/daily_article')
api.add_resource(BlogArticle, '/blog_article')
api.add_resource(BlogArticleDetail, '/<int:article_id>/blog_article')
api.add_resource(BlogTag, '/blog_tag')
api.add_resource(BlogTagDetail, '/<int:blog_tag_id>/blog_tag')
api.add_resource(BlogCategory, '/blog_category')
api.add_resource(BlogCategoryDetail, '/<int:blog_category_id>/blog_category')
