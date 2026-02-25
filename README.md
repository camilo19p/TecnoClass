# TecnoClass - Sistema de Gestión Académica

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)](https://docs.python.org/3/library/tkinter.html)
[![GitHub release](https://img.shields.io/github/v/release/camilo19p/TecnoClass)](https://github.com/camilo19p/TecnoClass/releases)

## 📋 Descripción

**TecnoClass** es una aplicación de escritorio desarrollada en **Python** que automatiza la administración escolar en instituciones educativas. El sistema permite gestionar estudiantes, profesores, notas y asistencia de manera eficiente, reemplazando procesos manuales por una solución digital.

---

## ✨ Características principales

- **Gestión de Estudiantes**: Matricular, expulsar, actualizar y visualizar datos de estudiantes
- **Gestión de Profesores**: Registrar, despedir, actualizar y visualizar datos de profesores
- **Control de Grados**: Organización por grados (6° a 11°)
- **Interfaz por consola**: Menús interactivos fáciles de usar
- **Persistencia de datos**: Almacenamiento en archivos JSON

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje**: Python 3.13+
- **Interfaz**: Consola / Tkinter (según versión)
- **Almacenamiento**: JSON (estudiantes.json, profesores.json)
- **Empaquetado**: PyInstaller para ejecutable
- **Control de versiones**: Git y GitHub

---

## 🖼️ Capturas de pantalla

| Menú principal | Selección de grado | Ingreso de datos |
|:--------------:|:------------------:|:----------------:|
| ![Menu](Capturas/captura1.png) | ![Grados](Capturas/captura2.png) | ![Ingreso](Capturas/captura3.png) |

> **Nota**: Las capturas están en la carpeta `/Capturas` del repositorio.

---

## 🚀 Cómo probar el programa

### Opción 1: Descargar el ejecutable (recomendado)
[![Download](https://img.shields.io/badge/Download-TecnoClass.exe-blue)](https://github.com/camilo19p/TecnoClass/releases)

1. Ve a la sección **[Releases](https://github.com/camilo19p/TecnoClass/releases)**
2. Descarga el archivo `TecnoClass.exe`
3. ¡Haz doble clic y ejecuta! (No necesitas instalar Python)

### Opción 2: Ejecutar desde el código fuente
```bash
# Clonar el repositorio
git clone https://github.com/camilo19p/TecnoClass.git

# Entrar a la carpeta
cd TecnoClass

# Ejecutar
python main.py
