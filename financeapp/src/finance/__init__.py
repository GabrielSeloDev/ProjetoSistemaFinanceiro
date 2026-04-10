from flask import Flask, render_template
from .extensions import init_extensions, db, migrate
from .config import Config 


    

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from .blueprints.usuarios import bp as usuarios_bp
    from .blueprints.pages import bp as pages_bp
    from .blueprints.categoria import bp as categorias_bp

    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(pages_bp)
    app.register_blueprint(categorias_bp, url_prefix='/categoria')

    from . import models



    return app
