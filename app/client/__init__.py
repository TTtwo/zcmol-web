from ..config import configs
from app.kernel.core import Core


def create_core(env: str) -> Core:
    from .controllers import controllers

    if env not in configs:
        raise ValueError('configs haven\'t %s' % env)

    core = Core(import_name=__name__, configs=configs[env].to_dict())

    for c in controllers:
        c.bind(core)

    return core
