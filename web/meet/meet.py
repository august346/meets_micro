from .bp import bp


def init_meet_bp(app):
    app.register_blueprint(bp)
    return bp
