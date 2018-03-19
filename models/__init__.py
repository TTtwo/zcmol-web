from .user import User
from .dailyarticle import DailyArticle
from .guestbook import Guestbook
from .link import Link
from .dailycomment import DailyComment
from ..kernel.database import DB

def create_all():
    DB.create_all()


