from kernel.database import DB
import datetime

class Link(DB.Model):

    __tablename__ = 'zc_links'

    link_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    link_name = DB.Column(DB.String(30), nullable=False)
    link_url = DB.Column(DB.String(150), nullable=False)
    create_at = DB.Column(DB.DateTime, nullable=False, default=datetime.datetime.now)

