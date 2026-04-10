from flask import render_template
from . import bp
from ...models import Usuario
from ...extensions import db
from flask import Blueprint, render_template, request, redirect, url_for

# Rota para Listar Usuários (O "READ" do CRUD)
@bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios)

@bp.get('/novo')
def criar_usuario():
    return render_template('usuarios/criar_usuario.html')

@bp.post('/novo')
def salvar_usuario():

    nome_digitado = request.form.get('nome')
    email_digitado = request.form.get('email')
    
    # Cria o usuário no banco de dados
    novo_usuario = Usuario(nome=nome_digitado, email=email_digitado)
    db.session.add(novo_usuario)
    db.session.commit()
    
    return redirect(url_for('usuarios.listar_usuarios'))

# Rota pra deletar o usuario
@bp.post('/<int:id>/deletar')
def deletar_usuario(id):
    # Procura o usuário pelo ID da URL
    usuario = Usuario.query.get_or_404(id)
    
    # Deleta do banco e salva
    db.session.delete(usuario)
    db.session.commit()
    
    # Redireciona de volta para a tabela de listagem de usuários
    return redirect(url_for('usuarios.listar_usuarios'))

@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_usuario(id):

    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':

        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        

        db.session.commit()
        return redirect(url_for('usuarios.listar_usuarios'))


    return render_template('usuarios/editar_usuario.html', usuario=usuario)