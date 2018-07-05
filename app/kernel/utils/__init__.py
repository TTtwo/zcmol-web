from .authorization import *
from .response import *
from .required import *


def to_seconds(*, hours=0, minutes=0, seconds=0) -> int:
    assert isinstance(hours, int)
    assert isinstance(minutes, int)
    assert isinstance(seconds, int)
    return hours * 3600 + minutes * 60 + seconds
