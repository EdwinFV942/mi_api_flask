from flask import Blueprint, jsonify
from models.categorias import Categoria
from models.cursos import Curso
from models.alumnos import Alumno


api_bp = Blueprint('api', __name__)

@api_bp.route('/categories', methods=['GET'])
def get_categories():
    """
    Obtener todas las categorías
    ---
    responses:
      200:
        description: Lista de todas las categorías registradas en la base de datos
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nombre:
                type: string
                example: "Programación"
    """
    # 1. Consultar todas las categorías usando SQLAlchemy
    categorias = Categoria.query.all()
    
    resultado = [categoria.to_dict() for categoria in categorias]
    
    return jsonify(resultado), 200

@api_bp.route('/categories/<int:id>/courses', methods=['GET'])
def get_courses_by_category(id):
    """Devuelve los cursos de una categoría
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Lista de cursos
    """
    cursos = Curso.query.filter(Curso.categoria_id == id).all()
    return jsonify([c.to_dict() for c in cursos])

@api_bp.route('/categories/<int:id>/courses/count', methods=['GET'])
def get_courses_count_by_category(id):
    """Devuelve cuántos cursos tiene una categoría
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Conteo de cursos
    """
    cantidad = Curso.query.filter(Curso.categoria_id == id).count()
    return jsonify({"categoria_id": id, "cantidad_cursos": cantidad})

@api_bp.route('/courses', methods=['GET'])
def get_courses():
    """Lista todos los cursos
    ---
    responses:
      200:
        description: Lista de cursos
    """
    cursos = Curso.query.all()
    return jsonify([c.to_dict() for c in cursos])

@api_bp.route('/courses/<int:id>/students', methods=['GET'])
def get_students_by_course(id):
    """Lista los alumnos inscritos en un curso
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Alumnos inscritos
    """
    alumnos = Alumno.query.filter(
        Alumno.cursos.any(Curso.id == id)
    ).all()

    return jsonify([a.to_dict() for a in alumnos])

@api_bp.route('/students', methods=['GET'])
def get_students():
    """Lista todos los alumnos
    ---
    responses:
      200:
        description: Lista de alumnos
    """
    alumnos = Alumno.query.all()
    return jsonify([a.to_dict() for a in alumnos])

@api_bp.route('/students/<int:id>/courses', methods=['GET'])
def get_courses_by_student(id):
    """Lista los cursos en los que está inscrito un alumno
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Cursos del alumno
    """
    alumno = Alumno.query.get(id)

    if not alumno:
        return jsonify({"error": "Alumno no encontrado"}), 404

    return jsonify([c.to_dict() for c in alumno.cursos])

@api_bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    """Endpoint clave: Alumnos y Cursos en los que están inscritos
    ---
    responses:
      200:
        description: Estructura de inscripciones
    """
    alumnos = Alumno.query.all()

    return [
        {
            "alumno": alumno.to_dict(),
            "cursos": [curso.to_dict() for curso in alumno.cursos]
        }
        for alumno in alumnos
    ]


