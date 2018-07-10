from flask import jsonify
from enum import Enum


class RespError(Enum):
    PASS = 0,
    FRE_COMMENT = 2001,


def resp_to_json(*args, **kwargs):
    if 'error' not in kwargs:
        error = RespError.PASS.value
        kwargs['error'] = error
    return jsonify(*args, **kwargs)
