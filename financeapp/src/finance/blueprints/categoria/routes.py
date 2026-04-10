from flask import render_template, request, redirect, url_for
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
    # NOVO: Busca usuários para o <select>
    usuarios = Usuario.query.all() 
    return render_template('categorias/criar_categoria.html', usuarios=usuarios)

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

# Rota para deletar categorias
@bp.post('/deletar/<int:id>')
def deletar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    
    db.session.delete(categoria)
    db.session.commit()
    
    # CORRIGIDO: Agora redireciona de volta para a lista corretamente
    return redirect(url_for('categoria.listar_categorias'))

# Rota para editar categorias
@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = Categoria.query.get_or_404(id)

    if request.method == 'POST':
        categoria.nome = request.form.get('nome')
        categoria.cor = request.form.get('cor')
        categoria.usuario_id = request.form.get('usuario_id')
        
        db.session.commit()
        return redirect(url_for('categoria.listar_categorias'))

    usuarios = Usuario.query.all()
    
    return render_template('categorias/editar_categoria.html', categoria=categoria, usuarios=usuarios)