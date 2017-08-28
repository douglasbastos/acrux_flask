from flask import Flask

from blueprints.noticias import noticias_blueprint
from db_config import db


db.connect()
app = Flask(__name__)
app.config.from_object('settings')

app.register_blueprint(noticias_blueprint, url_prefix='/portal')
