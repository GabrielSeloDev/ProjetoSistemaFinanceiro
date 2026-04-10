from flask import render_template
from . import bp
from ...models import Categoria
from ...extensions import db
from flask import Blueprint, render_template, request


#Rota para pagina para criar categoria

@bp.get('/novo')
def criar_categoria():
    return render_template('categorias/criar_categoria.html')

@bp.post('/novo')
def salvar_categoria():
    nome_cat = request.form.get('nome')
    cor_cat = request.form.get('cor')
    usuario_id = request.form.get('usuario_id')

    nova_categoria = Categoria(nome=nome_cat, cor=cor_cat, usuario_id=usuario_id)
    db.session.add(nova_categoria)
    db.session.commit()

    return render_template('pages/home.html')