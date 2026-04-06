from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate() 

def init_extensions (app):
    print('extensões inicializadas com sucesso')
