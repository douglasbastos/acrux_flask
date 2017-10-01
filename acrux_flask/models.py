from peewee import Model, CharField, TextField

from .db_config import db

# Noticia(db.DynamicDocument) não tem obrigatoriedade de schema
class Noticia(db.Document):
    titulo = db.StringField()
    texto = db.StringField()
    imagem = db.StringField()