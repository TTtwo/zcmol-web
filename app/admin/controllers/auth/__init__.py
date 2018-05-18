from admin.controllers.controller import AdminController
from flask import jsonify

auth_controller = AdminController(import_name=__name__, name='auth', prefix='/auth')
_a = auth_controller


@_a.get('/index')
def index():
    return jsonify({"code": 0})
