# 🧪 API Escolar: Categorías, Cursos y Alumnos

API REST desarrollada con Flask y documentada con Swagger, diseñada para gestionar una estructura académica.

---

## 📌 Requisitos Previos
- Python 3.8 o superior
- MySQL
- SQLite3 (opcional si decides cambiar la configuración)

---

## ⚠️ Configuración de Base de Datos

Esta API está configurada para trabajar con **MySQL** y utiliza variables de entorno (`.env`).

La conexión se construye dinámicamente en `config.py`.

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

---

## 🔐 Configurar Variables de Entorno (.env)

El proyecto utiliza variables de entorno para la conexión a la base de datos.

### Crear archivo `.env`

**En Windows:**
```bash
copy .env.example .env
```

**En Mac/Linux:**
```bash
cp .env.example .env
```

### Configurar valores

Edita el archivo `.env` con tus datos:

```env
nombre_db=nombre_de_tu_base_de_datos
usuario_db=usuario_de_tu_base_de_datos
password_db=tu_password
host_db=localhost
```

---

## 🗄️ Creación de Base de Datos

Crea la base de datos usando el mismo nombre que definiste en `.env`:

```sql
CREATE DATABASE nombre_de_tu_base_de_datos;
```

> ⚠️ Importante:  
El nombre de la base de datos debe coincidir con `nombre_db` en tu `.env`.

---

## 📦 Instalación de Dependencias

```bash
pip install -r requirements.txt
```

---

## 🚀 Inicialización del Proyecto

Una vez configurada la base de datos, ejecuta:

```bash
flask db upgrade
python seed.py
python app.py
```

---

## 📄 Documentación (Swagger)

Accede a la documentación en:

👉 http://127.0.0.1:5000/docs

---

## 📌 Notas Finales

- Asegúrate de que MySQL esté corriendo antes de iniciar la aplicación
- Verifica que tu archivo `.env` esté correctamente configurado
- Si tienes problemas con migraciones, puedes regenerarlas

---

## 👨‍💻 Autor

Proyecto desarrollado para fines académicos.
