from flask import Blueprint

bp = Blueprint('contas', __name__, template_folder='templates')

from . import routes