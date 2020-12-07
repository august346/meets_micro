from flask import Blueprint

from . import views

api_routes = (
    ('users', views.UserListView, views.UserApiView),
    ('players', views.PlayerListView, views.PlayerApiView),
    ('sessions', views.SessionListView, views.SessionApiView),
    ('phrases', views.PhraseListView, views.PhraseApiView),
    ('contents', views.ContentListView, views.ContentApiView),
)


def get_bp(app):
    bp = Blueprint('api', __name__)

    for name, list_view, api_view in api_routes:
        app.api.add_resource(list_view, f'/{name}')
        app.api.add_resource(api_view, f'/{name}/<obj_id>')

    app.register_blueprint(bp)

    return bp
