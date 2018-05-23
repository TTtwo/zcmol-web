def required_check_params(*validate_args: dict):
    def decorate(fn):
        def wrap(*args, **kwargs):
            return fn(*args, **kwargs)

        return wrap

    return decorate
