from flask import Flask

class Core:

    def __init__(self, import_name: str, configs: dict):

        self.app = Flask(import_name)
        self.app.config.update(configs)
        self.app.core = self
        self.plugins = {}


    # app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = ('mysql+mysqlconnector://root:root@127.0.0.1:3306/demo002')
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

