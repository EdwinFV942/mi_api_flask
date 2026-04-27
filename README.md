# 🧪 API Escolar: Categorías, Cursos y Alumnos

API REST desarrollada con Flask y documentada con Swagger, diseñada para gestionar una estructura académica.

---

## 📌 Requisitos Previos
- Python 3.8 o superior
- MySQL
- SQLite3 (opcional si decides cambiar la configuración)

---

## ⚠️ Configuración de Base de Datos

Esta API está configurada para trabajar con **MySQL**, por lo que debes:

1. Crear una base de datos en MySQL.
2. Configurar la conexión en tu archivo `config.py` o variables de entorno.

Ejemplo de conexión:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://usuario:password@localhost/nombre_bd"
```
---

## ⚙️ Instrucciones de Instalación y Ejecución

1. **Clonar el repositorio:**
```bash
git clone https://github.com/EdwinFV942/mi_api_flask.git
cd mi_api_flask
```

2. **Crear el entorno virtual:**
```bash
python -m venv venv
```

3. **Activar el entorno:**
```bash
# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

---

## 🚀 Inicialización del Proyecto

Una vez configurada la base de datos en MySQL y creada la DB `extraordinary`, ejecuta los siguientes comandos:

```bash
flask db upgrade
python seed.py
python app.py
```

---

## 📄 Documentación (Swagger)

Una vez que el servidor esté corriendo, abre tu navegador web y visita la siguiente ruta para probar los endpoints interactivamente:

👉 http://127.0.0.1:5000/docs

---

## 📌 Notas Finales

- Asegúrate de que MySQL esté corriendo antes de iniciar la aplicación.
- Verifica que las credenciales de la base de datos sean correctas.
- Si tienes problemas con migraciones, puedes eliminarlas y generarlas nuevamente.

---

## 👨‍💻 Autor

Proyecto desarrollado para fines académicos.
