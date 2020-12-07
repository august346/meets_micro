from flask import Flask
from flask_restful import Api

import settings
from datebase.models import *
from rest.bp import get_bp


def create_app():
    app = Flask(__name__)
    app.db = _init_db(app)
    app.api = _init_api(app)
    app.api.rest = get_bp(app)
    return app


def _init_db(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:postgres@{settings.DB_HOST}/meet'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db


def _init_api(app):
    return Api(app, prefix='/api')
