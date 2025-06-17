# 📋 FastAPI - ToDo API

Este proyecto es una API REST desarrollada con **FastAPI** que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre tareas. La persistencia de datos se realiza mediante **SQLite** y el ORM **SQLAlchemy**.

---

## 🐍 Requisitos
    
- Python 3.10
- Git (opcional para clonar el repo)


## 🚀 Funcionalidades

- ✅ Obtener todas las tareas.
- 🔍 Obtener una tarea por su ID.
- ➕ Crear una nueva tarea.
- ✏️ Actualizar una tarea existente.
- ❌ Eliminar una tarea.

---

## 🧱 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)
- SQLite (base de datos local)

---

## 📦 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/LucasNavarro01/ToDo.git
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

- En **Windows**:

```bash
.venv\Scripts\activate
```

- En **Linux/Mac**:

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Crear archivo `.env`

Crear un archivo `.env` en la raíz del proyecto (si no existe) con contenido como:

```env
DATABASE_URL=sqlite:///./tasks.db
LOG_LEVEL=INFO
```

### 6. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:  
📍 `http://127.0.0.1:8000`

La documentación automática está disponible en:  
🔹 Swagger UI → `http://127.0.0.1:8000/docs`  
🔹 ReDoc → `http://127.0.0.1:8000/redoc`

---

## 📁 Estructura del proyecto

```
.
├── app/
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── config.py            # Configuración de la base de datos
│   ├── models/              # Definición de los modelos de SQLAlchemy
│   ├── schemas/             # Esquemas de validación con Pydantic
│   ├── routers/             # Rutas de la API
│   └── services/            # Lógica del negocio
├── tasks.db                 # Base de datos SQLite
├── .env                     # Variables de entorno (no se sube a Git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Endpoints de ejemplo

### Obtener todas las tareas

```http
GET /tasks/
```

### Crear una nueva tarea

```http
POST /tasks/
```

Cuerpo del request (JSON):

```json
{
  "title": "Estudiar FastAPI",
  "description": "Practicar creando un CRUD",
  "completed": false
}
```

---

## 🧑‍💻 Autor

Desarrollado por Lucas Navarro

---
