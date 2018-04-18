from kernel.database import DB
import datetime


class DailyArticle(DB.Model):
    __tablename__ = 'zc_daily_article'
    da_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    da_title = DB.Column(DB.String(50), nullable=False)
    da_content = DB.Column(DB.Text(500))
    da_time = DB.Column(DB.DateTime, default=datetime.datetime.now)
    da_state = DB.Column(DB.Integer, default=0)
    da_content_pos = DB.Column(DB.Integer, default=0)
    da_browse_number = DB.Column(DB.Integer, default=0)


