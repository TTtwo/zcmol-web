from flask import jsonify
from enum import Enum


class RespError(Enum):
    PASS = 0,
    FRE_COMMENT = 2001,
    COMMENT_INVAILD = 2002,


def resp_to_json(*args, **kwargs):
    if 'error' not in kwargs:
        error = RespError.PASS.value
        kwargs['error'] = error[0]
    return jsonify(*args, **kwargs)
