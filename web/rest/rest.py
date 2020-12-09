from flask_restful import Api

from rest.bp import get_bp


def init_api(app):
    api = Api(app, prefix='/api')
    api.bp = get_bp(app, api)
    return api
