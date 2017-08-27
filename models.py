from peewee import Model, CharField, TextField

from db_config import db


class Noticia(Model):
    titulo = CharField()
    texto = TextField()
    imagem = CharField()

    class Meta:
        database = db

# Noticia.create_table()