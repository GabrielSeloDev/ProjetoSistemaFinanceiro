from flask import render_template, request, redirect, url_for
from . import bp
from ...extensions import db
from ...models import Conta, Usuario 

# Rota para listar as contas (READ)
@bp.get('/')
def listar_contas():
    contas = Conta.query.all()
    return render_template('contas/listar.html', contas=contas)

# Rota para página de criar (CREATE - GET)
@bp.get('/novo')
def criar_conta():
    usuarios = Usuario.query.all()
    return render_template('contas/criar_conta.html', usuarios=usuarios)

# Rota para salvar a conta (CREATE - POST)
@bp.post('/novo')
def salvar_conta():
    nome_digitado = request.form.get('nome')
    saldo_inicial = request.form.get('saldo_inicial', 0.0)
    usuario_id = request.form.get('usuario_id') 

    try:
        saldo_float = float(saldo_inicial)
    except ValueError:
        saldo_float = 0.0

    nova_conta = Conta(
        nome=nome_digitado, 
        saldo_inicial=saldo_float, 
        usuario_id=usuario_id
    )
    
    db.session.add(nova_conta)
    db.session.commit()

    return redirect(url_for('contas.listar_contas'))

# Rota para editar conta (UPDATE)
@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_conta(id):
    conta = Conta.query.get_or_404(id)

    if request.method == 'POST':
        conta.nome = request.form.get('nome')
        conta.usuario_id = request.form.get('usuario_id')
        
        try:
            conta.saldo_inicial = float(request.form.get('saldo_inicial', 0.0))
        except ValueError:
            pass # Mantém o antigo se der erro de digitação
        
        db.session.commit()
        return redirect(url_for('contas.listar_contas'))

    usuarios = Usuario.query.all()
    return render_template('contas/editar_conta.html', conta=conta, usuarios=usuarios)

# Rota para deletar conta (DELETE)
@bp.post('/deletar/<int:id>')
def deletar_conta(id):
    conta = Conta.query.get_or_404(id)
    db.session.delete(conta)
    db.session.commit()
    return redirect(url_for('contas.listar_contas'))