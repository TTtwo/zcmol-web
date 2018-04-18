def __fileter_attribute__(attr: str):
    return not attr.startswith('_') and attr != 'to_dict'


class SysConfig:

    # system
    DEBUG = False
    TESTING = False
    ENVIRONMENT = 'default'
    APP_NAME = ''
    SECRET_KEY = ''
    JWT_SECRET = ''

    # database
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    def to_dict(self):
        return {k: getattr(self, k) for k in dir(self) if __fileter_attribute__(k)}


