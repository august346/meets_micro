from flask import Blueprint

import views

api_routes = (
    ('users', views.UserListView, views.UserApiView),
    ('players', views.PlayerListView, views.PlayerApiView),
    ('sessions', views.SessionListView, views.SessionApiView),
    ('phrases', views.PhraseListView, views.PhraseApiView),
    ('contents', views.ContentListView, views.ContentApiView),
)


def add_api_routes(app):
    app.bp = Blueprint('api', __name__)

    for name, list_view, api_view in api_routes:
        list_route = f'/api/{name}'
        app.api.add_resource(list_view, list_route)
        app.api.add_resource(api_view, f'{list_route}/<obj_id>')

    app.register_blueprint(app.bp)
