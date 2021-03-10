Boilerplate (Django, Django REST Framework)

> Framework [Django 3.1.6](https://docs.djangoproject.com/en/3.1/releases/3.1/)

## Indice

* [Requisitos](#Requisitos)
* [Estructura Boilerplate](#Estructura)
* [Instalacion](#Instalacion)
* [Postman](#Postman)
* [Documentacion](#Documentacion)
* [Referencias](#Referencias)

## Requisitos

- VirtualEnv
- Python 3
- Pip
- PosgreSQL

## Paquetes extras
```
- Setuptools en caso de tener algun problema al estar instalando los requerimientos, 
tome en cuenta instalar estos paquetes de pip.
pip install setuptools
```

## Estructura del proyecto

```
boilerplate/
    venv/
        ...
    apps/
        user/
        assignCourse/
        courses/
        ... more apps here

    common/
        baseModel.py
        pagination.py
        utils.py

    project/
        __init__.py
        urls.py
        wsgi.py
        settings.py

     templates/

    .env.example
    SW.postman_collection.json
    SW-v1.postman_environment.json
    manage.py
    requirements.txt
```

## Instalacion
> Instalar requisitos anteriores,
> Descargar o clonar el proyecto.

```
# Crear entorno virtual (dentro del proyecto)
$ python3 -m venv venv

# Activar entorno virtual
$ source venv/bin/activate

# Desactivar
$ deactivate

# Copiar env de ejemplo y agregar datos
# Tenga en cuenta que necesita una BD en postgreSQL previamente creada
# indicando el nombre en el .env
cp .env.example .env
$ nano .env

# Instalar requerimientos (Con el entorno virtual activado)
$ pip install -r requirements.txt

# En caso de algun problema al instalar requerimientos tome en cuenta el siguiente comando
$ pip install setuptools
```

#### Comando extras
```
# Migraciones
$ python manage.py migrate

# Ejecutar proyecto
$ python manage.py runserver

# Ejecutar archivos estaticos
$ python manage.py collectstatic

# Crear un super usuario para accesar al panel de Django
$ python manage.py createsuperuser
```

## Estructura .ENV
```
DEBUG=
SECRET_KEY=
APP_NAME=
WEBSITE_URL=
SERVER_URL=
TIME_ZONE=
PAGINATION=

DB_ENGINE='django.db.backends.postgresql'
DB_HOST=
DB_NAME=
DB_OWNER=
DB_PASSWORD=
DB_PORT=

EMAIL_USE_TLS=
EMAIL=
EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_USER=
EMAIL_PASSWORD=
EMAIL_PORT=
```

## Doc Endpoint 
> Collection para importar a Postman para virualizar la carpeta de los endpoint.
```
SW.postman_collection.json
```
> Environment para tener acceso al host (http://127.0.0.1:8000/) y tambien obtener el access y refresh token para los endpoint que requiere autentificacion.
```
SW-v1.postman_environment.json
```

# Documentacion
```
El proyecto cuenta con 7 carpetas:
```
> Auth (Login)
```
Aqui agrego la logica de inicio de sesion asi como la de refresh para un token caducado
```
> Users (CRUD de usuarios (Alumnos y maestros))
```
Fitros: id, type, email

Aqui podemos registrar nuevos usuarios con un nivel de rol:
(1, ("Admin")),
(2, ("Teacher")),
(3, ("Student")),

Asi como:
-obtener a todos los usuarios
-Obtener a todos los alumnos
-Obtener a todos los maestros
-Obtener al usuarios loggeado
-Modificar un usuario
```
> Courses (CRUD de Coursos)
```
Fitros: id, title

Tenemos la logica para agregar cursos:
Ademas se implemento una logica para saber que tipo de usuario esta autenticado y con ello evitar que los alumnos tengan acceso a estos endpoints.
-Obtener cursos disponibles para estudiantes
-Obtener todos los cursos con sus lecciones, preguntas y respuestas
-Obtener solo los cursos
-Crear, Modificar, Eliminar
```
> Lessons (CRUD de lecciones)
```
Fitros: id, course

Logica para agregar lecciones
-Obtener lecciones disponibles para estudiantes
-Obtener todas las lecciones con sus preguntas y respuestas
-Obtener solo las lecciones
-Crear, Modificar, Eliminar
```
> Questions (CRUD de preguntas)
```
Fitros: id, lesson

Logica para agregar preguntas
-Obtener todas las preguntas
-Crear, Modificar, Eliminar
```
> Answers (CRUD de respuestas)
```
Fitros: id, question

Logica para agregar preguntas
-Obtener todas las respuestas
-Crear, Modificar, Eliminar
```
> Student_Assignment (Logica de asignacion de cursos)
```
Filtro: id, course, lesson

Toda la logica para alumnos
-Obtener todos los cursos de estudiantes
-Obtener todas las preguntas de los estudiantes
-Asignar un curso a un estudiante
-Actualizar un curso asignado a un estudiante
-Responder lecciones compeltas
```


# Referencias

* [Python 3](https://www.python.org/doc/)
* [Django 3](https://docs.djangoproject.com/es/3.1/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [PIP](https://pip.pypa.io/en/stable/)
* [Virtualenv](https://pypi.org/project/virtualenv/)
* [PostgreSQL](https://www.postgresql.org/)
* [JWT](https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8)
* [Environ](https://django-environ.readthedocs.io/en/latest/)