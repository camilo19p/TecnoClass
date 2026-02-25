import json
import os

# Archivos para almacenar datos
ARCHIVO_ESTUDIANTES = "estudiantes.json"
ARCHIVO_PROFESORES = "profesores.json"

# Estructuras de datos
estudiantes = []
profesores = []

def cargar_datos():
    """Carga los datos desde los archivos JSON"""
    global estudiantes, profesores
    
    if os.path.exists(ARCHIVO_ESTUDIANTES):
        with open(ARCHIVO_ESTUDIANTES, 'r', encoding='utf-8') as f:
            estudiantes = json.load(f)
    
    if os.path.exists(ARCHIVO_PROFESORES):
        with open(ARCHIVO_PROFESORES, 'r', encoding='utf-8') as f:
            profesores = json.load(f)

def guardar_datos():
    """Guarda los datos en los archivos JSON"""
    with open(ARCHIVO_ESTUDIANTES, 'w', encoding='utf-8') as f:
        json.dump(estudiantes, f, indent=2, ensure_ascii=False)
    
    with open(ARCHIVO_PROFESORES, 'w', encoding='utf-8') as f:
        json.dump(profesores, f, indent=2, ensure_ascii=False)

# Cargar datos al iniciar el módulo
cargar_datos()