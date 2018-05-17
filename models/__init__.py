from kernel.database import DB
from ..models.article.article import Article
from ..models.article.blog_content import BlogContent
from ..models.article.blog_content import BlogTag
from ..models.article.blog_content import BlogContentCategory
from ..models.article.daily_content import DailyContent
from ..models.article.article_comment import ArticleComment
from ..models.guestbook import GuestBook
from ..models.link import Link

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
