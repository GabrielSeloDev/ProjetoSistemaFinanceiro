from flask import Flask
from .extensions import init_extensions, db, migrate
from .config import Config 
# 1. ADICIONE ESTA LINHA AQUI EM CIMA
from .blueprints.usuarios import bp as usuarios_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)

    db.init_app(app)
    migrate.init_app(app, db)

# 2. ADICIONE ESTA LINHA AQUI DENTRO (antes do return app)
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

    from . import models


    @app.route("/")
    def home():
        return "Aplicação Funcionando"
    @app.route("/status")
    def status():
        return {"status": "ok"}

    return app
