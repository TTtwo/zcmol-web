from flask import jsonify


def resp_to_json(*args, **kwargs):
    return jsonify(*args, **kwargs)
