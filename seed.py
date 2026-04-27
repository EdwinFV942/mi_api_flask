import random
from app import create_app
from models import db
from models.categorias import Categoria
from models.cursos import Curso
from models.alumnos import Alumno

# Inicializamos la app para tener el contexto de la base de datos
app = create_app()

def run_seeder():
    with app.app_context():
        print("Iniciando el proceso de seeding...")

        # 1. Crear 2 Categorías
        cat_prog = Categoria(nombre="Programación")
        cat_diseno = Categoria(nombre="Diseño")
        db.session.add(cat_prog)
        db.session.add(cat_diseno)
        db.session.commit() # Guardamos para que se generen sus IDs
        print("✅ 2 Categorías creadas.")

        # 2. Crear 10 Cursos distribuidos en las categorías
        cursos_data = [
            ("Python Básico", cat_prog.id),
            ("Flask API", cat_prog.id),
            ("Java Avanzado", cat_prog.id),
            ("C++ para videojuegos", cat_prog.id),
            ("Desarrollo Web (HTML/CSS)", cat_prog.id),
            ("Photoshop desde cero", cat_diseno.id),
            ("Ilustración Digital", cat_diseno.id),
            ("UI/UX Fundamentals", cat_diseno.id),
            ("Edición de Video", cat_diseno.id),
            ("Figma Avanzado", cat_diseno.id)
        ]
        
        for nombre_curso, id_cat in cursos_data:
            nuevo_curso = Curso(nombre=nombre_curso, categoria_id=id_cat)
            db.session.add(nuevo_curso)
        db.session.commit()
        print("✅ 10 Cursos creados.")

        # 3. Crear 10 Alumnos
        nombres_alumnos = [
            "Juan Pérez", "Ana Gómez", "Carlos López", "María Silva", "Luis Torres",
            "Elena Martínez", "Pedro Ramírez", "Sofía Castro", "Diego Rojas", "Laura Vega"
        ]
        
        for nombre in nombres_alumnos:
            nuevo_alumno = Alumno(nombre=nombre)
            db.session.add(nuevo_alumno)
        db.session.commit()
        print("✅ 10 Alumnos creados.")

        # 4. Crear Relaciones (Inscripciones) aleatorias
        todos_los_cursos = Curso.query.all()
        todos_los_alumnos = Alumno.query.all()

        for alumno in todos_los_alumnos:
            # Seleccionar entre 1 y 3 cursos aleatorios para cada alumno
            cantidad_cursos = random.randint(1, 3)
            cursos_aleatorios = random.sample(todos_los_cursos, cantidad_cursos)
            
            for curso in cursos_aleatorios:
                # Gracias a la tabla intermedia inscripciones, SQLAlchemy hace la relación automáticamente
                alumno.cursos.append(curso)
        
        db.session.commit()
        print("✅ Inscripciones aleatorias generadas con éxito.")
        print("🚀 ¡La base de datos está lista!")

if __name__ == '__main__':
    run_seeder()