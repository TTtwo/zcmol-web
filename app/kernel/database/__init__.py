from flask_sqlalchemy import Model
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Pagination

DB = SQLAlchemy()


class ModelHelper:

    @staticmethod
    def serialize(model: Model):
        if model:
            model_data = {
                c.name: getattr(model, c.name)
                for c in model.__table__.columns
            }
            return model_data
        else:
            return {}
