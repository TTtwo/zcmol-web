from flask_sqlalchemy import Model
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

DB = SQLAlchemy()


def _serialize(data):
    return data.timestamp() if isinstance(data, datetime) else data


class ModelHelper:

    @staticmethod
    def serialize(model: Model, **kwargs):
        if model:
            if isinstance(model, dict) or isinstance(model, list):
                return model
            model_data = {
                c.name: _serialize(getattr(model, c.name))
                for c in model.__table__.columns
            }
            for key, value in kwargs.items():
                model_data[key] = ModelHelper.serialize(value) \
                    if not isinstance(value, list) \
                    else [
                    ModelHelper.serialize(v)
                    for v in value
                ]
            return model_data
        else:
            return {}

    @staticmethod
    def filter(model: Model, filter_keys: list):
        if model:
            for key in filter_keys:
                if key in model:
                    del model[key]
        return model
