from .db_config import db
from flask import Flask

from .blueprints.noticias import noticias_blueprint


def create_app(mode):
    db.connect()
    app = Flask(__name__)
    app.config.from_pyfile('{}.cfg'.format(mode))
    app.config.from_object('acrux_flask.settings')

    app.register_blueprint(noticias_blueprint, url_prefix='/portal')

    return app
