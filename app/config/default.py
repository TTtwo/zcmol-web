from app.kernel.core.sysconfig import SysConfig
from app.kernel.utils import to_seconds


class DefaultConfig(SysConfig):
    # sql-alchemy
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqlconnector://root:123456@127.0.0.1:3306/zcmol')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = '162.14.81.168'
    REDIS_PORT = 6379
    REDIS_PASS = ''
    REDIS_DB = 0
    REDIS_DEFAULT_EX = to_seconds(hours=24)
