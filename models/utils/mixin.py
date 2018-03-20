import datetime
from sqlalchemy.dialects.mysql import BIGINT
from kernel import DB

class ModelMinix:
    id = DB.Column(BIGINT(unsigned=True), nullable=False, unique=True,
                   primary_key=True, autoincrement=True)
    create_at = DB.Column(DB.DateTime(), nullable=False,
                          default=datetime.datetime.now)

class HelperMinix:

    id = None
    create_at = None
