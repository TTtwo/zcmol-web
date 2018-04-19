from flask import jsonify


class Response:
    @classmethod
    def _jsonify(cls, **kwargs):
        return jsonify(**kwargs)



