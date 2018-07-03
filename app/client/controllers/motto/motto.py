from app.kernel.database import DB
from app.kernel.database import ModelHelper
from app.models import Model
from app.kernel.utils.response import resp_to_json
from flask_restful import Resource
from flask_sqlalchemy import BaseQuery


class Motto(Resource):
    def get(self):
        motto: BaseQuery = Model \
            .Motto \
            .query \
            .filter_by(_hidden=False) \
            .order_by(Model.Motto.id.desc()) \
            .all()
        motto_items = [
            ModelHelper.serialize(item)
            for item in motto
        ]
        data = {'motto': motto_items}
        return resp_to_json(data=data)
