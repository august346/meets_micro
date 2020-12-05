from flask import Blueprint

import utils
import views

app = utils.create_app()

app.bp = Blueprint('api', __name__)
app.api.add_resource(views.UsersView, '/users')
app.api.add_resource(views.UserView, '/users/<obj_id>')
app.register_blueprint(app.bp)


@app.route('/')
def index():
    return 'Hello 2 world'


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)
