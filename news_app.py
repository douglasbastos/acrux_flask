from flask import Flask

from blueprints.noticias import noticias_blueprint
from db_config import db


def create_app(config_filename=None):
    db.connect()
    app = Flask(__name__)
    if config_filename:
        app.config.from_pyfile(config_filename)

    app.register_blueprint(noticias_blueprint, url_prefix='/portal')
