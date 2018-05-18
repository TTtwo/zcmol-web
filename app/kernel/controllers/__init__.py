from flask import Blueprint


class BaseController:
    REQUIRED_ENV = None

    def __init__(self, import_name, name, prefix, template_folder=None):

        self.blueprint = Blueprint(name=name, import_name=import_name, url_prefix=prefix,
                                   template_folder=template_folder)
        self.import_name = import_name
        self.name = name
        self.prefix = prefix

    def bind(self, core):
        """　bind controller to app,　and register relevant event"""
        app = core.app
        if self.REQUIRED_ENV:
            env = app.config["ENVIRONMENT"]
            if env != self.REQUIRED_ENV:
                return False
        app.register_blueprint(self.blueprint)
        return True

    def _router(self, route, method, **options):
        """ bind view func to blueprint"""

        def decorator(fn):
            options['methods'] = [method]
            return self.blueprint.route(route, **options)(fn)

        return decorator

    def get(self, route, **options):
        return self._router(route, 'GET', **options)

    def post(self, route, **options):
        return self._router(route, 'POST', **options)

    def login_required(self):
        # TODO
        pass

    def visit_limit(self, seconds):
        # TODO
        pass
