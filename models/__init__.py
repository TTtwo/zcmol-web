from models.user import User
from models.dailyarticle import DailyArticle
from models.guestbook import Guestbook
from models.link import Link
from models.dailycomment import DailyComment
from kernel.database import DB

def create_all():
    DB.create_all()


