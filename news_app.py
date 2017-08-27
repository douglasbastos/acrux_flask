from flask import Flask

from db_config import db

db.connect()
app = Flask(__name__)
app.config.from_object('settings')

import views
