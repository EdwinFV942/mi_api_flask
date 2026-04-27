-- seed.sql
-- Insertar 2 Categorías obligatorias
INSERT INTO categorias (nombre) VALUES 
('Programación'), 
('Diseño');

-- Insertar 10 Cursos (Asignados a los IDs 1 y 2 de las categorías)
INSERT INTO cursos (nombre, categoria_id) VALUES 
('Python Básico', 1),
('Flask API', 1),
('Java Avanzado', 1),
('C++ para videojuegos', 1),
('Desarrollo Web (HTML/CSS)', 1),
('Photoshop desde cero', 2),
('Ilustración Digital', 2),
('UI/UX Fundamentals', 2),
('Edición de Video', 2),
('Figma Avanzado', 2);

-- Insertar 10 Alumnos
INSERT INTO alumnos (nombre) VALUES 
('Juan Pérez'), 
('Ana Gómez'), 
('Carlos López'), 
('María Silva'), 
('Luis Torres'),
('Elena Martínez'), 
('Pedro Ramírez'), 
('Sofía Castro'), 
('Diego Rojas'), 
('Laura Vega');

-- Generar Inscripciones (Relaciones Alumnos - Cursos)
INSERT INTO inscripciones (alumno_id, curso_id) VALUES 
(1, 1), (1, 2), (1, 5),   -- Juan Pérez en 3 cursos
(2, 6), (2, 7),           -- Ana Gómez en 2 cursos
(3, 3), (3, 4),           -- Carlos López en 2 cursos
(4, 1), (4, 8),           -- María Silva en 2 cursos
(5, 9), (5, 10),          -- Luis Torres en 2 cursos
(6, 2), (6, 5),           -- Elena Martínez en 2 cursos
(7, 1), (7, 4),           -- Pedro Ramírez en 2 cursos
(8, 8), (8, 10),          -- Sofía Castro en 2 cursos
(9, 3), (9, 4),           -- Diego Rojas en 2 cursos
(10, 6), (10, 9);         -- Laura Vega en 2 cursos