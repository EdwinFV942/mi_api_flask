from models import db

class Curso(db.Model):
    __tablename__ = 'cursos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    categoria_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'categoria_id': self.categoria_id
        }