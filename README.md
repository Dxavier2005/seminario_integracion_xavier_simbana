# Seminario de Integración

**Autor:** Xavier Simbaña

## Descripción

Este repositorio está destinado a la materia **Seminario de Integración**, en la cual se realizará un repaso y fortalecimiento de conocimientos sobre herramientas y tecnologías utilizadas en el desarrollo de software, enfocándose en el desarrollo backend y frontend.

Se trabajará con Python, uv, FastAPI y Angular, reforzando conceptos fundamentales, configuraciones de entorno, desarrollo de aplicaciones y la integración entre los diferentes componentes de un sistema de software.

## Objetivo

Repasar y fortalecer los conocimientos sobre Python, uv, FastAPI y Angular mediante ejercicios prácticos y actividades de desarrollo, comprendiendo la función de cada tecnología y su aplicación en la construcción e integración de aplicaciones web.

## Tecnologías utilizadas

### 1. Python

**Concepto:** Python es un lenguaje de programación de alto nivel, conocido por su sintaxis clara y facilidad de aprendizaje.

**¿Para qué sirve?**
- Desarrollar aplicaciones y automatizar tareas.
- Procesar y analizar datos.
- Crear servicios backend y API.
- Implementar la lógica de una aplicación.

### 2. uv

**Concepto:** uv es una herramienta rápida para gestionar paquetes, dependencias y entornos de proyectos Python.

**¿Para qué sirve?**
- Crear y administrar entornos virtuales.
- Instalar y gestionar dependencias.
- Mantener un registro de dependencias mediante `uv.lock`.
- Sincronizar el entorno de desarrollo con la configuración del proyecto.

**Comandos básicos:**

```bash
uv init
uv venv
uv add fastapi
uv sync
```

### 3. FastAPI

**Concepto:** FastAPI es un framework de Python utilizado para construir API web de forma rápida, con validación de datos y documentación automática.

**¿Para qué sirve?**
- Crear servicios backend.
- Definir rutas y endpoints.
- Recibir y responder solicitudes HTTP.
- Validar datos mediante modelos.
- Conectar aplicaciones con bases de datos y otros servicios.

**Ejemplo de aplicación:** desarrollar una API que permita consultar, registrar, actualizar y eliminar información.

### 4. Angular

**Concepto:** Angular es un framework de desarrollo frontend que permite crear aplicaciones web dinámicas utilizando TypeScript, componentes y servicios.

**¿Para qué sirve?**
- Crear interfaces de usuario.
- Organizar aplicaciones mediante componentes.
- Gestionar formularios y navegación.
- Consumir API mediante solicitudes HTTP.
- Mostrar información obtenida desde el backend.

**Ejemplo de aplicación:** crear una interfaz web que consuma los endpoints desarrollados con FastAPI.

## Integración de las tecnologías

Las tecnologías se pueden combinar para desarrollar una aplicación web completa:

1. **Angular:** presenta la interfaz con la que interactúa el usuario.
2. **FastAPI:** recibe las solicitudes del frontend y proporciona los servicios backend.
3. **Python:** implementa la lógica de negocio de la API.
4. **uv:** administra las dependencias y el entorno de desarrollo de Python.

## Estructura del proyecto

```text
seminario-integracion/
├── README.md
├── .gitignore
├── backend/
│   ├── pyproject.toml
│   ├── uv.lock
│   └── main.py
└── frontend/
    └── proyecto-angular/
        ├── package.json
        ├── angular.json
        └── src/
```

*Nota: esta estructura es una propuesta inicial y puede modificarse según las actividades y los requerimientos de la materia.*

## Herramientas de desarrollo

- **Git:** sistema de control de versiones para registrar cambios en el código.
- **GitHub:** plataforma para alojar repositorios y colaborar en proyectos.
- **Visual Studio Code:** editor de código para trabajar con Python, TypeScript y otras tecnologías.
- **Terminal:** permite ejecutar comandos para configurar, desarrollar y probar las aplicaciones.

## Conclusión

El desarrollo de esta materia permitirá reforzar los fundamentos de programación y comprender cómo se relacionan las herramientas del backend y frontend. El propósito es adquirir una base práctica para desarrollar, organizar e integrar aplicaciones web utilizando tecnologías modernas.