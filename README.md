# Librark - Gestión de E-commerce de Libros

**Librark** comenzó como un pequeño emprendimiento de venta de libros y artículos para lectores. Debido a su enfoque en la atención al cliente, la plataforma ha evolucionado para consolidarse como un sistema de gestión integral que ofrece una experiencia de compra excepcional, abarcando desde clásicos hasta los éxitos literarios más recientes.

---

## 🚀 Funcionalidades Principales

### 📚 Gestión del Catálogo (App: Libros)
*   **Exploración:** Listado completo de libros con filtros de búsqueda por título y autor.
*   **Administración:** CRUD completo (Crear, Leer, Actualizar, Eliminar) para la gestión del inventario de libros.
*   **Acceso Restringido:** Las funciones de creación, edición y eliminación están protegidas mediante el decorador `@login_required` y `LoginRequiredMixin`.

### 👥 Usuarios y Perfiles (App: Usuarios)
*   **Seguridad:** Sistema de registro, inicio y cierre de sesión basado en las herramientas de autenticación de Django.
*   **Personalización:** Cada usuario posee un perfil único con avatar, información personal y hobbies.
*   **Autogestión:** Interfaz para que el usuario actualice sus datos personales y cambie su contraseña de forma segura.

### 📧 Atención al Cliente (App: About)
*   **Contacto:** Formulario dinámico para que los clientes envíen consultas directamente a la administración.
*   **Gestión de Consultas:** Panel exclusivo para usuarios autenticados que permite visualizar y gestionar (eliminar) los mensajes recibidos.
*   **Misión:** Sección dedicada a la historia y valores de Librark.

---

## 🛠️ Tecnologías Utilizadas
*   **Framework:** Django 6.0.4.
*   **Base de Datos:** SQLite.
*   **Manejo de Imágenes:** Pillow 12.2.0 (para el procesamiento de avatares y portadas).
*   **Entorno:** Python 3.13 con manejo de variables de entorno mediante `python-dotenv`.

---

## 🔧 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/mahkzi/Python-Django.git
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Preparar la base de datos:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Crear cuenta de administrador:**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Iniciar la aplicación:**
    ```bash
    python manage.py runserver
    ```

---

## 📂 Estructura del Proyecto
*   `/config`: Configuraciones de proyecto y rutas globales.
*   `/libros`: Lógica de negocio para el catálogo de la librería.
*   `/usuarios`: Manejo de cuentas de usuario, seguridad y perfiles extendidos.
*   `/about`: Módulo informativo, formularios de contacto y gestión de envíos.

---
*Este proyecto fue desarrollado como parte de la entrega final del curso de Python.*
