from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }