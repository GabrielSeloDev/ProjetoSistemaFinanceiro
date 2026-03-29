from flask import Flask
from .extensions import init_extensions

def create_app():
    app = Flask(__name__)

    init_extensions(app)


    @app.route("/")
    def home():
        return "Aplicação funcionando"
    @app.route("/status")
    def status():
        return {"status": "ok"}

    return app
