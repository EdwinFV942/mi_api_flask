import os

class Config:
    # Obtener variables desde .env
    DB_NAME = os.getenv('nombre_db', 'extraordinary')
    DB_USER = os.getenv('usuario_db', 'root')
    DB_PASSWORD = os.getenv('password_db', '')
    DB_HOST = os.getenv('host_db', 'localhost')

    # Construir la URI dinámicamente
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de Swagger
    SWAGGER = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs"
    }