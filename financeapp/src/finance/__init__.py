from flask import Flask
from .extensions import init_extensions, db, migrate
from .config import Config 



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)

    db.init_app(app)
    migrate.init_app(app, db)


    from . import models


    @app.route("/")
    def home():
        return "Aplicação Funcionando"
    @app.route("/status")
    def status():
        return {"status": "ok"}

    return app
