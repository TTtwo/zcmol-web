from .link import Link
from ..kernel.database import DB
from .guestbook import GuestBook
from .motto import Motto
from .article.article import Article
from .article.blog_content import BlogTag
from .article.blog_content import BlogContent
from .article.daily_content import DailyContent
from .article.article_comment import ArticleComment
from .article.blog_content import BlogContentCategory


class Model:
    Article = Article
    ArticleComment = ArticleComment
    BlogTag = BlogTag
    BlogContent = BlogContent
    BlogContentCategory = BlogContentCategory
    DailyContent = DailyContent
    GuestBook = GuestBook
    Motto = Motto
    Link = Link

    def create_all(self):
        DB.create_all()

# MODELS = {
#     "Article": Article,
#     "ArticleComment": ArticleComment,
#     "BlogContentCategory": BlogContentCategory,
#     "BlogTag": BlogTag,
#     "BlogContent": BlogContent,
#     "DailyContent": DailyContent,
#     "GuestBook": GuestBook,
#     "Link": Link,
# }
