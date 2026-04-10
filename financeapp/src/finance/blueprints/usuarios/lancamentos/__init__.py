from flask import Blueprint

# Cria o blueprint de lançamentos
lancamentos_bp = Blueprint('lancamentos', __name__)

# Importa as rotas para conectá-las ao blueprint
from . import routes