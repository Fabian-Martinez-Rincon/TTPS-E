import os
import typing as t
from dotenv import load_dotenv


class ConfigurationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

def env_or_error(env: str, default: t.Union[str, None] = None) -> str:
    value = os.getenv(env, default)
    if value is None:
        raise ConfigurationError(f"Environment variable '{env}' not set")
    return value

class Config:
    # Flask-livetw config
    LIVETW_DEV: bool
    TESTING = False
    #Configurar la carga de imagenes
    UPLOAD_FOLDER = 'Char-IT/static/'
    ALLOWED_EXTENSIONS = {'png', 'PNG', 'jpg', 'JPG'}
    # Configurar la extensión Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'hopeTrade08@gmail.com'
    MAIL_PASSWORD = 'hgju fnoc xpfg rrwp'  # para ingresar a GMAIL: 08_hopeTrade
    MAIL_DEFAULT_SENDER = 'hopeTrade08@gmail.com'
    
    @classmethod
    def load_env_config(cls) -> None:
        cls.LIVETW_DEV = env_or_error("LIVETW_ENV", "production").lower() == "development"

class ProductionConfig(Config):
    """Production configuration"""

class DevelopmentConfig(Config):
    """Development configuration"""
    DB_USER = os.getenv("DB_USER")
    load_dotenv()
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST") 
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_TRACK_NOTIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    LIVETW_DEV=True
    

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True

config = {"production": ProductionConfig,"development": DevelopmentConfig,"testing": TestingConfig}


