from kernel.database import DB
import datetime

class DailyComment(DB.Model):

    __tablename__ = 'zc_daily_comment'

    daco_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    daco_user = DB.Column(DB.Integer, nullable=False)
    daco_time = DB.Column(DB.DateTime, default=datetime.datetime.now)
    daco_content = DB.Column(DB.String(500))
    daco_ip = DB.Column(DB.String(30))
    daco_reply_id = DB.Column(DB.Integer, DB.ForeignKey('zc_daily_comment.daco_id'), nullable=True)
    da_id = DB.Column(DB.Integer, DB.ForeignKey('zc_daily_article.da_id'), nullable=False)

