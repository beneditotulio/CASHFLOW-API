import os
from flask import Flask
from flask_cors import CORS
from config import Config
from .extensions import db, jwt
from .routes import api


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    CORS(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    db.init_app(app)
    jwt.init_app(app)

#registar o blueprint com as rotas da API
    app.register_blueprint(api, url_prefix='/api')

    #criar as tabelas do banco de dados
    with app.app_context():
        db.create_all()

    return app