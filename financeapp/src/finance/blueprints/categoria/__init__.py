from flask import Blueprint

bp = Blueprint('categoria', __name__)

from . import routes

