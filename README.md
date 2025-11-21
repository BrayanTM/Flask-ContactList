# Flask-ContactList 📇

Aplicación de Lista de Contactos desarrollada con Flask utilizando API REST. Este proyecto implementa un sistema CRUD completo para gestionar contactos con persistencia en base de datos PostgreSQL.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Migraciones de Base de Datos](#migraciones-de-base-de-datos)
- [Licencia](#licencia)

## ✨ Características

- ✅ API RESTful completa para gestión de contactos
- ✅ Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- ✅ Validación de datos de entrada
- ✅ Prevención de duplicados (email y teléfono únicos)
- ✅ Soporte para actualizaciones parciales (PATCH)
- ✅ Base de datos PostgreSQL con Docker
- ✅ Migraciones de base de datos con Flask-Migrate
- ✅ Respuestas JSON estructuradas
- ✅ Manejo de errores HTTP apropiado

## 🛠️ Tecnologías

- **Flask 3.1.2** - Framework web
- **Flask-SQLAlchemy 3.1.1** - ORM para base de datos
- **Flask-Migrate 4.1.0** - Migraciones de base de datos
- **PostgreSQL 18** - Base de datos
- **psycopg2-binary 2.9.11** - Adaptador PostgreSQL
- **python-dotenv 1.2.1** - Gestión de variables de entorno
- **Docker & Docker Compose** - Contenedorización

## 📦 Requisitos Previos

- Python 3.14 o superior
- Docker y Docker Compose
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/BrayanTM/Flask-ContactList.git
cd Flask-ContactList
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -e .
```

## ⚙️ Configuración

### 1. Crear archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Flask Configuration
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True

# Database Configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=tu_password_aqui
POSTGRES_DB=contacts_db
POSTGRES_PORT=5432

# Database URL
DATABASE_URL=postgresql://postgres:tu_password_aqui@localhost:5432/contacts_db
```

### 2. Iniciar la base de datos con Docker

```bash
docker-compose up -d
```

Esto iniciará un contenedor PostgreSQL en el puerto 5432.

### 3. Ejecutar migraciones

```bash
flask db upgrade
```

## 💻 Uso

### Iniciar la aplicación

```bash
python main.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🔌 API Endpoints

### Base URL
```
http://localhost:5000/api/v1/contacts
```

### Endpoints Disponibles

#### 1. Obtener todos los contactos
```http
GET /api/v1/contacts/
```

**Respuesta exitosa (200):**
```json
{
  "contacts": [
    {
      "id": 1,
      "name": "Juan Pérez",
      "email": "juan@example.com",
      "phone": "+51987654321"
    }
  ]
}
```

**Sin contactos (404):**
```json
{
  "message": "No contacts found"
}
```

#### 2. Obtener un contacto por ID
```http
GET /api/v1/contacts/<contact_id>
```

**Respuesta exitosa (200):**
```json
{
  "contact": {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "+51987654321"
  }
}
```

**No encontrado (404):**
```json
{
  "message": "Contact not found"
}
```

#### 3. Crear un nuevo contacto
```http
POST /api/v1/contacts/
Content-Type: application/json
```

**Body:**
```json
{
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "phone": "+51987654321"
}
```

**Respuesta exitosa (201):**
```json
{
  "message": "Contact added successfully",
  "contact": {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "+51987654321"
  }
}
```

**Datos faltantes (400):**
```json
{
  "message": "Name, email, and phone are required"
}
```

**Duplicado (409):**
```json
{
  "message": "Contact with this email or phone already exists"
}
```

#### 4. Actualizar un contacto (completo)
```http
PUT /api/v1/contacts/<contact_id>
Content-Type: application/json
```

**Body:**
```json
{
  "name": "Juan Pérez Actualizado",
  "email": "juan.nuevo@example.com",
  "phone": "+51987654322"
}
```

**Respuesta exitosa (200):**
```json
{
  "message": "Contact updated successfully",
  "contact": {
    "id": 1,
    "name": "Juan Pérez Actualizado",
    "email": "juan.nuevo@example.com",
    "phone": "+51987654322"
  }
}
```

#### 5. Actualizar un contacto (parcial)
```http
PATCH /api/v1/contacts/<contact_id>
Content-Type: application/json
```

**Body (solo campos a actualizar):**
```json
{
  "phone": "+51999999999"
}
```

**Respuesta exitosa (200):**
```json
{
  "message": "Contact partially updated successfully",
  "contact": {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "+51999999999"
  }
}
```

#### 6. Eliminar un contacto
```http
DELETE /api/v1/contacts/<contact_id>
```

**Respuesta exitosa (200):**
```json
{
  "message": "Contact deleted successfully"
}
```

## 📁 Estructura del Proyecto

```
Flask-ContactList/
├── contactsapp/              # Paquete principal de la aplicación
│   ├── __init__.py          # Inicialización de la app Flask
│   ├── contacts.py          # Blueprint con rutas de la API
│   ├── db_con.py            # Configuración de SQLAlchemy
│   └── models.py            # Modelos de base de datos
├── migrations/               # Migraciones de base de datos
│   ├── versions/            # Versiones de migraciones
│   ├── alembic.ini          # Configuración de Alembic
│   ├── env.py               # Entorno de migraciones
│   └── script.py.mako       # Template para migraciones
├── config.py                 # Configuración de la aplicación
├── main.py                   # Punto de entrada de la aplicación
├── docker-compose.yml        # Configuración de Docker
├── pyproject.toml           # Dependencias del proyecto
├── README.md                # Este archivo
└── .env                     # Variables de entorno (no incluido)
```

## 🔄 Migraciones de Base de Datos

### Crear una nueva migración

Después de modificar los modelos:

```bash
flask db migrate -m "Descripción del cambio"
```

### Aplicar migraciones

```bash
flask db upgrade
```

### Revertir una migración

```bash
flask db downgrade
```

### Ver historial de migraciones

```bash
flask db history
```

## 📝 Modelo de Datos

### Contact

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | Integer | Primary Key, Auto-increment |
| name | String(100) | Not Null |
| email | String(100) | Unique, Not Null |
| phone | String(20) | Unique, Not Null |

## 🧪 Ejemplos de Uso con cURL

### Crear un contacto
```bash
curl -X POST http://localhost:5000/api/v1/contacts/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Juan Pérez","email":"juan@example.com","phone":"+51987654321"}'
```

### Obtener todos los contactos
```bash
curl http://localhost:5000/api/v1/contacts/
```

### Obtener un contacto específico
```bash
curl http://localhost:5000/api/v1/contacts/1
```

### Actualizar un contacto
```bash
curl -X PUT http://localhost:5000/api/v1/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Juan Pérez Updated","email":"juan.new@example.com","phone":"+51987654322"}'
```

### Actualización parcial
```bash
curl -X PATCH http://localhost:5000/api/v1/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{"phone":"+51999999999"}'
```

### Eliminar un contacto
```bash
curl -X DELETE http://localhost:5000/api/v1/contacts/1
```

## 🐳 Docker

### Comandos útiles

```bash
# Iniciar contenedores
docker-compose up -d

# Detener contenedores
docker-compose down

# Ver logs
docker-compose logs -f

# Reiniciar base de datos
docker-compose restart db
```

## 🔍 Solución de Problemas

### Error de conexión a la base de datos

1. Verifica que Docker esté corriendo: `docker ps`
2. Revisa las credenciales en `.env`
3. Asegúrate de que el puerto 5432 no esté en uso

### Error en las migraciones

```bash
# Eliminar todas las migraciones y empezar de nuevo
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**BrayanTM**

- GitHub: [@BrayanTM](https://github.com/BrayanTM)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub
