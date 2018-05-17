from kernel.database import DB
from .article.article import Article
from .article.blog_content import BlogContent
from .article.blog_content import BlogTag
from .article.blog_content import BlogContentCategory
from .article.daily_content import DailyContent
from .article.article_comment import ArticleComment
from .guestbook import GuestBook
from .link import Link

MODELS = {
    "Article": Article,
    "ArticleComment": ArticleComment,
    "BlogContentCategory": BlogContentCategory,
    "BlogTag": BlogTag,
    "BlogContent": BlogContent,
    "DailyContent": DailyContent,
    "GuestBook": GuestBook,
    "Link": Link,
}


def create_all():
    DB.create_all()
