from flask import Blueprint

bp = Blueprint('tb_usuario', __name__)

from . import routes