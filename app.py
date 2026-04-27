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
    
    # Inicializar Swagger con la configuración y un template de información
    swagger_template = {
        "info": {
            "title": "API Escolar REST",
            "description": "API para gestionar Categorías, Cursos y Alumnos.",
            "version": "1.0.0"
        }
    }
    Swagger(app, config=app.config['SWAGGER'], template=swagger_template)

    # Registrar las rutas
    app.register_blueprint(api_bp)

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"mensaje": "API funcionando. Visita /docs para ver Swagger."})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)