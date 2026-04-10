from flask import render_template, request, redirect, url_for
from . import bp
from ...extensions import db
# NOVO: Importamos o Usuario aqui também
from ...models import Lancamento, Categoria, Conta, Usuario

# Rota para listar os lançamentos
@bp.get('/')
def listar_lancamentos():
    lancamentos = Lancamento.query.all()
    return render_template('lancamentos/listar.html', lancamentos=lancamentos)

# Rota para pagina para criar lançamento
@bp.get('/novo')
def criar_lancamento():
    categorias = Categoria.query.all()
    contas = Conta.query.all() 
    # NOVO: Busca usuários para o <select>
    usuarios = Usuario.query.all()
    return render_template('lancamentos/criar_lancamento.html', categorias=categorias, contas=contas, usuarios=usuarios)

# Rota de salvamento dos dados do lançamento
@bp.post('/novo')
def salvar_lancamento():
    valor_digitado = request.form.get('valor')
    tipo_digitado = request.form.get('tipo')
    nome_digitado = request.form.get('nome')
    categoria_id = request.form.get('categoria_id') 
    usuario_id = request.form.get('usuario_id') 
    conta_id = request.form.get('conta_id') 

    try:
        valor_float = float(valor_digitado)
        if valor_float < 0:
            categorias = Categoria.query.all()
            contas = Conta.query.all()
            usuarios = Usuario.query.all() # <-- Busca para manter o HTML funcionando
            return render_template('lancamentos/criar_lancamento.html', categorias=categorias, contas=contas, usuarios=usuarios, erro="O valor não pode ser negativo!")
    except:
         categorias = Categoria.query.all()
         contas = Conta.query.all()
         usuarios = Usuario.query.all() # <-- Busca para manter o HTML funcionando
         return render_template('lancamentos/criar_lancamento.html', categorias=categorias, contas=contas, usuarios=usuarios, erro="Digite um número válido!")
        
    if tipo_digitado not in ['entrada', 'saida']:
        categorias = Categoria.query.all()
        contas = Conta.query.all()
        usuarios = Usuario.query.all() # <-- Busca para manter o HTML funcionando
        return render_template('lancamentos/criar_lancamento.html', categorias=categorias, contas=contas, usuarios=usuarios, erro="O tipo deve ser 'entrada' ou 'saida'!")

    novo_lancamento = Lancamento(
        valor=valor_float, 
        tipo=tipo_digitado, 
        nome=nome_digitado,
        categoria_id=categoria_id,
        usuario_id=usuario_id,
        conta_id=conta_id 
    )
    
    db.session.add(novo_lancamento)
    db.session.commit()

    return redirect(url_for('lancamentos.listar_lancamentos'))

# Rota para deletar lançamento
@bp.post('/deletar/<int:id>')
def deletar_lancamento(id):
    lancamento = Lancamento.query.get_or_404(id)
    db.session.delete(lancamento)
    db.session.commit()
    return redirect(url_for('lancamentos.listar_lancamentos'))

# Rota para alterar lançamento
@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_lancamento(id):
    lancamento = Lancamento.query.get_or_404(id)

    if request.method == 'POST':
        try:
            valor_float = float(request.form.get('valor'))
            if valor_float < 0:
                categorias = Categoria.query.all()
                contas = Conta.query.all()
                usuarios = Usuario.query.all() # <-- Busca para manter o HTML funcionando
                return render_template('lancamentos/editar_lancamento.html', lancamento=lancamento, categorias=categorias, contas=contas, usuarios=usuarios, erro="O valor não pode ser negativo!")
        except:
             categorias = Categoria.query.all()
             contas = Conta.query.all()
             usuarios = Usuario.query.all() # <-- Busca para manter o HTML funcionando
             return render_template('lancamentos/editar_lancamento.html', lancamento=lancamento, categorias=categorias, contas=contas, usuarios=usuarios, erro="Digite um número válido!")
            
        tipo_digitado = request.form.get('tipo')
        if tipo_digitado not in ['entrada', 'saida']:
            categorias = Categoria.query.all()
            contas = Conta.query.all()
            usuarios = Usuario.query.all() # <-- Busca para manter o HTML funcionando
            return render_template('lancamentos/editar_lancamento.html', lancamento=lancamento, categorias=categorias, contas=contas, usuarios=usuarios, erro="O tipo deve ser 'entrada' ou 'saida'!")

        lancamento.valor = valor_float
        lancamento.tipo = tipo_digitado
        lancamento.nome = request.form.get('nome')
        lancamento.categoria_id = request.form.get('categoria_id')
        lancamento.usuario_id = request.form.get('usuario_id')
        lancamento.conta_id = request.form.get('conta_id')
        
        db.session.commit()
        return redirect(url_for('lancamentos.listar_lancamentos'))

    categorias = Categoria.query.all()
    contas = Conta.query.all()
    # NOVO: Busca usuários para o <select>
    usuarios = Usuario.query.all()
    return render_template('lancamentos/editar_lancamento.html', lancamento=lancamento, categorias=categorias, contas=contas, usuarios=usuarios)