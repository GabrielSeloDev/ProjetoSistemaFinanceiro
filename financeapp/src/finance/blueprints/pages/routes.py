from flask import render_template
from . import bp

#Rotas 

@bp.get('/')
def home():
    return render_template('pages/home.html')

@bp.get("/sobre")
def sobre():
    return render_template("pages/sobre.html")