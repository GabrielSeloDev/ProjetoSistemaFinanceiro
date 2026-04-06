from .extensions import db
from sqlalchemy.sql import func
from sqlalchemy import Enum

class Usuario(db.Model):
    __tablename__ = 'tb_usuario'


    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    #Relacionamentos
    contas = db.relationship('Conta', backref='usuario')
    categorias = db.relationship('Categoria', backref='usuario')
    lancamentos = db.relationship('Lancamento', backref='usuario')

class Conta(db.Model):
    __tablename__ = 'tb_conta'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'), nullable=False)

    #Relacionamento
    lancamentos = db.relationship('Lancamento', backref='conta')
    
class Categoria(db.Model):
    __tablename__ = 'tb_categoria'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    cor = db.Column(db.String(20), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'), nullable=False)

    #Relacionamento
    lancamentos = db.relationship('Lancamento', backref='categoria')

class Lancamento(db.Model):
    __tablename__ = 'tb_lancamento'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    data = db.Column(db.DateTime, nullable=False, server_default=func.now())
    tipo =  db.Column(Enum('entrada', 'saida', name='tipoLancamento'), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'), nullable=False)
    conta_id = db.Column(db.Integer, db.ForeignKey('tb_conta.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('tb_categoria.id'), nullable=False)
