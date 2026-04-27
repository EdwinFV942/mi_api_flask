from flask import Flask, jsonify
from flasgger import Swagger
from config import Config
from routes.api import api_bp
from flask_migrate import Migrate

# 👇 IMPORTANTE: importar db desde models (NO desde cada modelo)
from models import db
from models.categorias import Categoria
from models.cursos import Curso
from models.alumnos import Alumno

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)
    migrate.init_app(app, db)

    # Configuración de Swagger
    swagger_template = {
        "info": {
            "title": "API Escolar REST",
            "description": "API para gestionar Categorías, Cursos y Alumnos.",
            "version": "1.0.0"
        }
    }

    Swagger(app, config=app.config.get('SWAGGER', {}), template=swagger_template)

    # Registrar rutas
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({
            "mensaje": "API funcionando correctamente",
            "docs": "/docs"
        })

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)