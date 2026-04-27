from models import db

class inscripciones(db.Model):
    __tablename__ = 'inscripciones'
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), primary_key=True)

    def to_dict(self):
        return {
            'alumno_id': self.alumno_id,
            'curso_id': self.curso_id
        }