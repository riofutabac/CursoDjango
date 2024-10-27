# Curso Django desde Cero 🐍

## Índice
- [1. Introducción a Django](#1-introducción-a-django)
- [1.2. Bases de Datos y Configuración Inicial](#12-bases-de-datos-y-configuración-inicial)
- [1.3. Primera Página con Django](#13-primera-página-con-django)
- [1.4. Parámetros en Django](#14-parámetros-en-django)

## 1. Introducción a Django

Django es un framework de Python que nos permite crear sitios web complejos de forma rápida y sencilla. Su principal ventaja es que nos ayuda a automatizar tareas repetitivas y comunes en el desarrollo web.

### Patrón MTV (Model-Template-View)

Django se basa en una variación del patrón MVC (Modelo-Vista-Controlador) llamada MTV (Model-Template-View):

- **Model (Modelo)**: Maneja todo lo relacionado con los datos y la base de datos
- **Template (Plantilla)**: Es lo que el usuario ve (el equivalente a la Vista en MVC)
- **View (Vista)**: Actúa como controlador, gestionando la lógica y la comunicación entre el modelo y el template

#### Flujo de una petición en Django:
1. El usuario hace una petición desde un formulario web
2. La petición es recibida por la Vista (View)
3. La Vista procesa la petición y solicita datos al Modelo si es necesario
4. El Modelo devuelve los datos procesados
5. La Vista renderiza el Template con los datos
6. El usuario recibe la respuesta

Esta arquitectura hace que nuestras aplicaciones sean:
- Funcionales
- Mantenibles
- Escalables

> 💡 **Nota**: Mientras que otros frameworks como Laravel, Symfony o CodeIgniter usan MVC directamente, Django usa MTV manteniendo la misma filosofía pero con nombres diferentes.

## 1.2. Bases de Datos y Configuración Inicial

### Bases de Datos Soportadas
Django soporta oficialmente cuatro bases de datos:
- PostgreSQL
- MySQL
- Oracle
- SQLite

También existe soporte comunitario para otras bases de datos SQL y NoSQL.

### Creación de un Proyecto

Para crear un nuevo proyecto Django:
```bash
django-admin startproject nombreProyecto
```

#### Estructura del Proyecto
```
nombreProyecto/
    ├── manage.py
    └── nombreProyecto/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

- **manage.py**: Utilidad que nos permite interactuar con el proyecto
- **__init__.py**: Indica a Python que la carpeta debe tratarse como un paquete
- **settings.py**: Contiene todas las configuraciones del proyecto
- **urls.py**: Define las URLs del proyecto
- **wsgi.py**: Configuración para el servidor web

### Aplicaciones Instaladas por Defecto
En `settings.py` encontramos:
```python
INSTALLED_APPS = [
    'django.contrib.admin',        # Panel de administración
    'django.contrib.auth',         # Sistema de autenticación
    'django.contrib.contenttypes', # Framework para tipos de contenido
    'django.contrib.sessions',     # Framework de sesiones
    'django.contrib.messages',     # Framework de mensajes
    'django.contrib.staticfiles',  # Manejo de archivos estáticos
]
```

### Inicialización del Proyecto
```bash
python manage.py migrate
```
Este comando crea las tablas necesarias en la base de datos (por defecto SQLite3) para las aplicaciones instaladas.

### Servidor de Desarrollo
```bash
python manage.py runserver
```
> ⚠️ **Advertencia**: El servidor de desarrollo no está diseñado para producción. No soporta múltiples sesiones ni cargas de trabajo pesadas.

## 1.3. Primera Página con Django

Para crear nuestra primera página necesitamos:
1. Crear una vista
2. Configurar la URL

### Creando una Vista Simple
En `views.py`:
```python
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola Mundo!")
```

> 📝 **Nota**: Cada función en views.py se considera una vista y debe recibir como mínimo el parámetro `request`.

### Configurando URLs
En `urls.py`:
```python
from django.contrib import admin
from django.urls import path
from .views import saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
]
```

## 1.4. Parámetros en Django

### Contenido Dinámico
Podemos enviar HTML y contenido dinámico en nuestras vistas:

```python
import datetime

def dameFecha(request):
    fechaActual = datetime.datetime.now()
    
    documentoHtml = """
    <html>
    <body>
        <h1>Fecha y Hora: %s</h1>
    </body>
    </html>
    """ % fechaActual
    
    return HttpResponse(documentoHtml)
```

### Parámetros en URLs
Django implementa URLs amigables (URL friendly) que son fáciles de leer y mantener.

Ejemplo de vista con parámetros:
```python
def calculaEdad(request, anio):
    edadActual = datetime.datetime.today().year - anio
    return HttpResponse(f"<h1>Tu edad es: {edadActual}</h1>")
```

Configuración en `urls.py`:
```python
path('edades/<int:anio>', calculaEdad)
```

> 💡 **Tip**: El patrón `<int:anio>` indica que esperamos un número entero en la URL que se pasará como parámetro `anio` a nuestra vista.

---

## 📚 Recursos Adicionales
- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Tutorial oficial de Django](https://docs.djangoproject.com/en/stable/intro/tutorial01/)