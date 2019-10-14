from flask_restful import Resource, Api

api = Api()


def init_app(app):
    api.app = app
    from . import auth, todo
    auth.init_app(api)
    todo.init_app(api)
