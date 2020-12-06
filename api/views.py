from http import HTTPStatus

from flask import jsonify, request, make_response
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash

from datebase import models


def api_view_function(f):
    def wrapper(view, obj_id):
        if obj := view.model.query.get(obj_id):
            return f(view, obj)
        abort(404)

    return wrapper


class DefaultView(Resource):
    model = None

    def __init__(self):
        if self.model is None:
            raise NotImplementedError('View `model` undefined!')


class DefaultListView(DefaultView):

    def get(self):
        return jsonify(list(map(
            lambda u: u.to_dict(),
            self.model.query.all()
        )))

    def post(self):
        json = request.get_json()
        json['password'] = generate_password_hash(json['password'], 'sha256')

        models.db.session.add(obj := self.model(**json))
        models.db.session.commit()

        return make_response(
            jsonify(id=obj.id),
            HTTPStatus.CREATED
        )


class DefaultApiView(DefaultView):

    @api_view_function
    def get(self, obj):
        return obj.to_dict()

    @api_view_function
    def put(self, obj):
        for key, value in request.get_json().items():
            setattr(obj, key, value)

        models.db.session.add(obj)
        models.db.session.commit()

        return make_response(
            jsonify(obj.to_dict()),
            HTTPStatus.OK
        )

    @api_view_function
    def delete(self, obj):
        models.db.session.delete(obj)
        models.db.session.commit()

        return make_response(
            jsonify(id=obj.id),
            HTTPStatus.NO_CONTENT
        )


class UserListView(DefaultListView):
    model = models.User


class UserApiView(DefaultApiView):
    model = models.User


class PlayerListView(DefaultListView):
    model = models.Player


class PlayerApiView(DefaultApiView):
    model = models.Player


class SessionListView(DefaultListView):
    model = models.Session


class SessionApiView(DefaultApiView):
    model = models.Session


class PhraseListView(DefaultListView):
    model = models.Phrase


class PhraseApiView(DefaultApiView):
    model = models.Phrase


class ContentListView(DefaultListView):
    model = models.Content


class ContentApiView(DefaultApiView):
    model = models.Content
