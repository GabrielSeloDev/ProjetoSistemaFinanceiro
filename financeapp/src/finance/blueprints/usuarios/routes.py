from flask import render_template
from . import bp
from ...models import Usuario
from ...extensions import db
from flask import Blueprint, request, jsonify, render_template

# Rota para Listar Usuários (O "READ" do CRUD)
@bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    # Se você estiver usando templates HTML:
    #return render_template('usuarios.html', usuarios=usuarios)
    # Se for apenas API:
    return jsonify([{"id": u.id, "nome": u.nome} for u in usuarios]), 200

# Rota para Criar Usuário (O "CREATE" do CRUD)
@bp.route('/novo', methods=['POST'])
def criar_usuario():
    dados = request.json # Pega os dados enviados
    novo_usuario = Usuario(nome=dados['nome'], email=dados['email'])
    
    db.session.add(novo_usuario)
    db.session.commit() # Salva no banco [cite: 54]
    
    return jsonify({"mensagem": "Usuário criado!"}), 201
