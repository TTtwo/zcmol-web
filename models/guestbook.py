from kernel.database import DB
import datetime


class GuestBook(DB.Model):
    __tablename__ = 'zc_guestbook'
    gu_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    gu_content = DB.Column(DB.String(100), nullable=False)
    gu_my_reply = DB.Column(DB.String(100))
    gu_time = DB.Column(DB.DateTime, nullable=False, default=datetime.datetime.now)
    gu_ip = DB.Column(DB.String(30))
    gu_email_avater = DB.Column(DB.String(150))
