from flask import Flask, render_template
from .extensions import init_extensions, db, migrate
from .config import Config 
from .blueprints.usuarios import bp as usuarios_bp
from src.finance.blueprints.pages.routes import bp as pages_bp

    

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)

    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

        
    app.register_blueprint(pages_bp)

    from . import models



    return app
