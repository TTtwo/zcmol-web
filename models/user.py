import datetime
from kernel.database import DB

class User(DB.Model):
    __tablename__ = 'zc_user'
    user_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    user_name = DB.Column(DB.String(20), nullable=False, unique=True)
    user_password = DB.Column(DB.String(20), nullable=False)
    user_level = DB.Column(DB.Integer, default=1, nullable=False)
    user_email = DB.Column(DB.String(30), )
    user_is_delete = DB.Column(DB.Integer, nullable=False, default=0)
    create_at = DB.Column(DB.DateTime, default=datetime.datetime.now, nullable=False)


