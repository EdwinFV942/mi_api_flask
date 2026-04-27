from models import db, inscripciones

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)

    cursos = db.relationship('Curso', secondary=inscripciones, lazy='subquery',
        backref=db.backref('alumnos', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }