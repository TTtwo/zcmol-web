from flask import Blueprint



class BaseController():

    REQUIRED_ENV = None

    def __init__(self, import_name, name, prefix, template_folder=None):

        self.bluprint = Blueprint(name, import_name, )

        self.import_name = import_name
        self.name = name
        self.prefix = prefix

        def _handle_err(err):
            return err

    def bind(self, core):
        """　bind controller to app,　and register relevant event"""
        app = core.app
        if self.REQUIRED_ENV:
            env = app.config["ENVIROMENT"]
            if env != self.REQUIRED_ENV:
                return False
        app.register_blueprint(self.bluprint)
        return True

    def _router(self, route, method, **options):
        """ bind view func to blueprint"""
        def decorater(fn):
            options['methods'] = [method]
            return self.bluprint.route(route, **options)(fn)

        return decorater

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































