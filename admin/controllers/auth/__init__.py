from ..controller import AdminController
from flask import jsonify

auth_controller = AdminController(__name__, 'demo', '/auth')
_a = auth_controller

@_a.get('/index')
def index():
    return jsonify({"code": 0})