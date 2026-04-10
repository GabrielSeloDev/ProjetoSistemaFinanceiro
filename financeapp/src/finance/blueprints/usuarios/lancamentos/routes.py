from flask import request, jsonify
from . import lancamentos_bp
from src.finance.extensions import db
from src.finance.models import Categoria # E o modelo de Lançamento que você tiver criado

@lancamentos_bp.route('/novo', methods=['POST'])
def criar_lancamento():
    dados = request.json
    valor = dados.get('valor')
    tipo = dados.get('tipo')
    
    # ==========================================
    # REGRA DE NEGÓCIO 1: Não aceitar valor negativo
    # ==========================================
    if valor is None or float(valor) < 0:
        return jsonify({"erro": "O valor do lançamento não pode ser negativo!"}), 400
        
    # ==========================================
    # REGRA DE NEGÓCIO 2: Só aceitar 'entrada' ou 'saida'
    # ==========================================
    if tipo not in ['entrada', 'saida']:
        return jsonify({"erro": "O tipo deve ser exclusivamente 'entrada' ou 'saida'!"}), 400

    # Se passou pelas regras, cria o lançamento no banco (Ajuste conforme o seu models.py)
    # novo_lancamento = Lancamento(valor=valor, tipo=tipo, descricao=dados.get('descricao'))
    # db.session.add(novo_lancamento)
    # db.session.commit()

    return jsonify({"mensagem": "Lançamento criado com sucesso!"}), 201