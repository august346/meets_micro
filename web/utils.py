from flask import Flask

import settings
from datebase.models import *
from meet import meet
from rest import rest


def create_app():
    app = Flask(__name__)
    app.db = _init_db(app)
    app.rest_api = rest.init_api(app)
    app.meet_api = meet.init_meet_bp(app)
    return app


def _init_db(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:postgres@{settings.DB_HOST}/meet'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db
