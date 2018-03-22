from kernel.core.sysconfig import SysConfig

class DefaultConfig(SysConfig):

    SQLALCHEMY_URI = ('mysql+mysqlconnector://root:root@127.0.0.1:3306/demo002')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

