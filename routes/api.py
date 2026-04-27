from flask import Blueprint, jsonify
from models import categorias, cursos, alumnos

api_bp = Blueprint('api', __name__)

@api_bp.route('/categories', methods=['GET'])
def get_categories():
    """Lista todas las categorías
    ---
    responses:
      200:
        description: Lista de categorías
    """
    return jsonify(categorias.obtener_todas())

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
    return jsonify(cursos.obtener_por_categoria(id))

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
    cantidad = cursos.contar_por_categoria(id)
    return jsonify({"categoria_id": id, "cantidad_cursos": cantidad})

@api_bp.route('/courses', methods=['GET'])
def get_courses():
    """Lista todos los cursos
    ---
    responses:
      200:
        description: Lista de cursos
    """
    return jsonify(cursos.obtener_todos())

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
    return jsonify(alumnos.obtener_por_curso(id))

@api_bp.route('/students', methods=['GET'])
def get_students():
    """Lista todos los alumnos
    ---
    responses:
      200:
        description: Lista de alumnos
    """
    return jsonify(alumnos.obtener_todos())

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
    return jsonify(alumnos.obtener_cursos_por_alumno(id))

@api_bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    """Endpoint clave: Alumnos y Cursos en los que están inscritos
    ---
    responses:
      200:
        description: Estructura de inscripciones
    """
    return jsonify(alumnos.obtener_inscripciones())


