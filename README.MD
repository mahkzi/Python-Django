# Librark - Gestión de E-commerce de Libros

**Librark** comenzó como un pequeño emprendimiento de venta de libros y artículos para lectores[cite: 38]. Debido a su enfoque en la atención al cliente, la plataforma ha evolucionado para consolidarse como un sistema de gestión integral que ofrece una experiencia de compra excepcional, abarcando desde clásicos hasta los éxitos literarios más recientes[cite: 38].

---

## 🚀 Funcionalidades Principales

### 📚 Gestión del Catálogo (App: Libros)
*   **Exploración:** Listado completo de libros con filtros de búsqueda por título y autor[cite: 37].
*   **Administración:** CRUD completo (Crear, Leer, Actualizar, Eliminar) para la gestión del inventario de libros[cite: 36, 37].
*   **Acceso Restringido:** Las funciones de creación, edición y eliminación están protegidas mediante el decorador `@login_required` y `LoginRequiredMixin`[cite: 37].

### 👥 Usuarios y Perfiles (App: Usuarios)
*   **Seguridad:** Sistema de registro, inicio y cierre de sesión basado en las herramientas de autenticación de Django[cite: 32].
*   **Personalización:** Cada usuario posee un perfil único con avatar, información personal y hobbies[cite: 33, 34].
*   **Autogestión:** Interfaz para que el usuario actualice sus datos personales y cambie su contraseña de forma segura[cite: 33].

### 📧 Atención al Cliente (App: About)
*   **Contacto:** Formulario dinámico para que los clientes envíen consultas directamente a la administración[cite: 39, 40].
*   **Gestión de Consultas:** Panel exclusivo para usuarios autenticados que permite visualizar y gestionar (eliminar) los mensajes recibidos[cite: 39, 40].
*   **Misión:** Sección dedicada a la historia y valores de Librark[cite: 38].

---

## 🛠️ Tecnologías Utilizadas
*   **Framework:** Django 6.0.4[cite: 35]
*   **Base de Datos:** SQLite[cite: 35]
*   **Manejo de Imágenes:** Pillow 12.2.0 (para el procesamiento de avatares y portadas)[cite: 35]
*   **Entorno:** Python 3.13 con manejo de variables de entorno mediante `python-dotenv`[cite: 35].

---

## 🔧 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/mahkzi/Blog-Python.git](https://github.com/mahkzi/Blog-Python.git)
    cd Blog-Python
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
*   `/config`: Configuraciones de proyecto y rutas globales[cite: 32].
*   `/libros`: Lógica de negocio para el catálogo de la librería[cite: 36, 37].
*   `/usuarios`: Manejo de cuentas de usuario, seguridad y perfiles extendidos[cite: 31, 33].
*   `/about`: Módulo informativo, formularios de contacto y gestión de envíos[cite: 39, 40].

---
*Este proyecto fue desarrollado como parte de la entrega final del curso de Python.*
