from app.kernel.core.sysconfig import SysConfig
from app.kernel.utils import to_seconds


class DefaultConfig(SysConfig):
    # sql-alchemy
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqlconnector://root@127.0.0.1:3306/zcmol')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = '123.207.123.241'
    REDIS_PORT = 6379
    REDIS_PASS = '123456'
    REDIS_DB = 0
    REDIS_DEFAULT_EX = to_seconds(hours=24)
