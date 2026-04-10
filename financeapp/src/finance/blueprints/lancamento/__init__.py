from flask import Blueprint

bp = Blueprint('lancamento', __name__)

from . import routes

