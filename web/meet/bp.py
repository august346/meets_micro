from http import HTTPStatus

from flask import Blueprint, jsonify
from flask_restful import abort

from datebase.models import Phrase, Content

bp = Blueprint('meet', __name__, url_prefix='/meet')


@bp.route('/questions/<int:session_id>')
def questions(session_id):
    phrases = map(
        lambda x: x.to_dict(),
        Phrase.query.filter(
            Phrase.session_id == session_id,
            Phrase.question_id.is_(None)
        )
    )

    return jsonify(list(phrases))


@bp.route('/answers/<int:question_id>')
def answers(question_id):
    phrases = map(
        lambda x: x.to_dict(),
        Phrase.query.filter(Phrase.question_id == question_id)
    )

    return jsonify(list(phrases))


@bp.route('/content/<int:content_id>')
def content(content_id):
    if (content_ := Content.query.get(content_id)) is None:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify(content_.file_name)
