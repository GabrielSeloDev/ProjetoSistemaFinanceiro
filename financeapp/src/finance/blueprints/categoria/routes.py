from flask import render_template, request, redirect, url_for # <-- Adicionei redirect e url_for aqui!
from . import bp
from ...models import Categoria, Usuario
from ...extensions import db

# Rota para listar as categorias
@bp.get('/')
def listar_categorias():
    categorias = Categoria.query.join(Usuario).order_by(Usuario.nome, Categoria.nome).all()
    return render_template('categorias/listar.html', categorias=categorias)

# Rota para pagina para criar categoria
@bp.get('/novo')
def criar_categoria():
    return render_template('categorias/criar_categoria.html')

# Rota de salvamento dos dados da categoria
@bp.post('/novo')
def salvar_categoria():
    nome_cat = request.form.get('nome')
    cor_cat = request.form.get('cor')
    usuario_id = request.form.get('usuario_id')

    nova_categoria = Categoria(nome=nome_cat, cor=cor_cat, usuario_id=usuario_id)
    db.session.add(nova_categoria)
    db.session.commit()

    return redirect(url_for('categoria.listar_categorias'))

@bp.post('/deletar/<int:id>')
def deletar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    
    db.session.delete(categoria)
    db.session.commit()
    
    
    return redirect(url_for('categoria.listar_categorias'))