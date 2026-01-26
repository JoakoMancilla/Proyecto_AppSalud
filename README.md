#🏥 App de Salud – Sistema de Gestión Clínica

Aplicación web orientada a la gestión de información médica, desarrollada con Django, que permite el acceso mediante distintos perfiles de usuario, el registro de anamnesis y la visualización de información a través de un dashboard centralizado.

Este proyecto fue desarrollado como una solución completa, integrando backend, base de datos y lógica de permisos, simulando un entorno real de una aplicación del área de la salud.
---
#🎥 Demo del proyecto (fase temprana)

📺 https://www.youtube.com/watch?v=FwiJjRK-kiA

Nota: el video muestra una etapa temprana del desarrollo; el proyecto actualmente se encuentra en fase terminada.
---
#🚀 Características principales
#🔐 Autenticación y roles de usuario

Acceso mediante distintos perfiles (administrador, médico y enfermero), cada uno con permisos específicos.

#📊 Dashboard interactivo

Panel principal con visualización clara de la información relevante según el rol del usuario.

#📝 Registro de Anamnesis

Sistema para crear, almacenar y consultar anamnesis de pacientes de forma estructurada.

#🗄️ Base de datos relacional

Persistencia de datos mediante modelos Django y ORM.

#⚙️ Arquitectura escalable

Backend preparado para crecer y adaptarse a nuevas funcionalidades.

#🛠️ Tecnologías utilizadas

Backend: Django (Python)

Base de datos: MySQL

Autenticación: Sistema de usuarios y permisos de Django

ORM: Django ORM

Frontend: Templates de Django / HTML / CSS
---
#⚙️ Instalación y puesta en marcha
git clone https://github.com/JoakoMancilla/Proyecto_AppSalud.git
cd Proyecto_AppSalud
pip install -r requirements.txt


Crear la base de datos en MySQL Workbench.

Configurar nombre de la base de datos, usuario, contraseña y puerto en settings.py.

Ejecutar migraciones:

python manage.py migrate


Crear desde el panel admin los usuarios:

Administrador

Médico

Enfermero

Las contraseñas se manejan mediante MD5 (por requisitos del proyecto).

Cargar datos iniciales:

python manage.py cargar_pacientes
python manage.py cargar_camas


Al cargar las camas, se debe asignar manualmente el área o especialidad (UCI, Urgencias, UTI, Ginecología, etc.).

Ejecutar el proyecto:

python manage.py runserver


Acceder desde el navegador a:
👉 http://127.0.0.1:8000/
---
🎯 Objetivo del proyecto

Simular un sistema real del área de la salud, aplicando buenas prácticas de desarrollo backend, manejo de datos sensibles y control de accesos, utilizando Django como framework principal.

📌 Estado del proyecto

✅ Proyecto finalizado
🛠️ Posibles mejoras futuras: API REST, frontend desacoplado, mayor nivel de seguridad y auditoría.

👨‍💻 Autor

Desarrollado por Joako Mancilla
Backend Developer / Web Developer
