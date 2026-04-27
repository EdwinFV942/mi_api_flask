from flask import Flask, jsonify, request
from flasgger import Swagger
from config import Config
from routes.api import api_bp
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar el blueprint de la API
    app.register_blueprint(api_bp, url_prefix='/api')

    # Configurar Swagger
    Swagger(app)
    @app.route('/')
    def home():
        return { "message": "api"}
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)