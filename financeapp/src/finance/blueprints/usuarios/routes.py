from flask import render_template
from . import bp
from ...models import Usuario
from ...extensions import db
from flask import Blueprint, render_template, request, jsonify

# Rota para Listar Usuários (O "READ" do CRUD)
@bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    # Se você estiver usando templates HTML:
    #return render_template('usuarios.html', usuarios=usuarios)
    # Se for apenas API:
    return jsonify([{"id": u.id, "nome": u.nome} for u in usuarios]), 200

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
    
    # Manda de volta pra Home 
    return render_template('pages/home.html')