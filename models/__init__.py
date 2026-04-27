from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabla intermedia requerida para la relación alumnos - cursos
inscripciones = db.Table('inscripciones',
    db.Column('alumno_id', db.Integer, db.ForeignKey('alumnos.id'), primary_key=True),
    db.Column('curso_id', db.Integer, db.ForeignKey('cursos.id'), primary_key=True)
)