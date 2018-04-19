from models.user import User
from models.dailyarticle import DailyArticle
from models.guestbook import GuestBook
from models.link import Link
from models.dailycomment import DailyComment
from kernel.database import DB

MODELS = {
    "User": User,
    "DailyArticle": DailyArticle,
    "GuestBook": GuestBook,
    "Link": Link,
    "DailyComment": DailyComment,
}

def create_all():
    DB.create_all()


