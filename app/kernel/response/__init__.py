from flask import jsonify


class Response:
    @staticmethod
    def to_json(**kwargs):
        return jsonify(**kwargs)
