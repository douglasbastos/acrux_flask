import os

from flask import request, current_app, render_template, send_from_directory, \
    Blueprint
from werkzeug.utils import secure_filename

from ..models import Noticia

noticias_blueprint = Blueprint('noticias', __name__)


@noticias_blueprint.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        dados_do_formulario = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename

        noticia = Noticia.objects.create(**dados_do_formulario)
        return render_template('cadastro_sucesso.html',
                               id_nova_noticia=noticia.id)

    return render_template('cadastro.html', title="Inserir nova noticia")


@noticias_blueprint.route("/")
def index():
    todas_as_noticias = Noticia.objects.all()
    return render_template('index.html',
                           noticias=todas_as_noticias,
                           title="Todas as notícias")


@noticias_blueprint.route("/noticia/<noticia_id>")
def noticia(noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    return render_template('noticia.html', noticia=noticia)


@noticias_blueprint.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)
