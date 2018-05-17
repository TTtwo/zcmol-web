from kernel.core.sysconfig import SysConfig


class DefaultConfig(SysConfig):
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqlconnector://root@127.0.0.1:3306/zcmol')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
