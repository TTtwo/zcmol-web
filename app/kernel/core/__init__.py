from flask import Flask
from ..database import DB
from flask_cors import CORS


class Core:
    def __init__(self, import_name: str, configs: dict):
        self.app = Flask(import_name)
        self.app.config.update(configs)
        self.app.core = self
        self.plugins = {}

        # init database
        DB.init_app(self.app)
        # 同源
        CORS(self.app)
