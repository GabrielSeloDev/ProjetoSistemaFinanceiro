from .extensions import db
from sqlalchemy.sql import func
from sqlalchemy import Enum

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.String(100), nullable=False)
