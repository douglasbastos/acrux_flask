import os

from flask import request, current_app, render_template, send_from_directory
from werkzeug.utils import secure_filename

from models import Noticia
from news_app import app


@app.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        dados_do_formulario = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename

        noticia = Noticia.create(**dados_do_formulario)
        return render_template('cadastro_sucesso.html',
                               id_nova_noticia=noticia.id)

    return render_template('cadastro.html', title="Inserir nova noticia")


@app.route("/")
def index():
    todas_as_noticias = Noticia.select()
    return render_template('index.html',
                           noticias=todas_as_noticias,
                           title="Todas as notícias")


@app.route("/noticia/<int:noticia_id>")
def noticia(noticia_id):
    noticia = Noticia.get(Noticia.id == noticia_id)
    return render_template('noticia.html', noticia=noticia)


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)
