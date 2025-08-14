import os
from dotenv import load_dotenv

# carregar variáveis de ambiente do ficheiro .env
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///cashflow.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Configurações específicas do SQLite
    SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,
    'pool_recycle': 3600,
    'connect_args': {
        'check_same_thread': False,  # Necessário para uso com SQLite em múltiplas
        'timeout': 20  # Tempo de espera para bloqueio
       }
    }

    # Configurações do JWT
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "default-jwt-secret-key")