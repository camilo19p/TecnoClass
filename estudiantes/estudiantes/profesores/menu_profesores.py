import os
from estudiantes.estudiantes import datos

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def ver_profesores():
    """Muestra la lista de todos los profesores"""
    limpiar_pantalla()
    print("Lista de profesores registrados en la institución:")
    
    if datos.profesores:
        for profesor in datos.profesores:
            print(profesor)
    else:
        print("No hay profesores registrados.")
    
    input("\nPresione Enter para continuar...")

def registrar_profesor():
    """Registra un nuevo profesor"""
    limpiar_pantalla()
    print("Ingrese los datos requeridos")
    nombre = input("Ingrese nombre del profesor: ")
    edad = input("Ingrese Edad: ")
    identificacion = input("Ingrese su número de identificación: ")
    asignatura = input("Ingrese la asignatura a dictar: ")
    
    nuevo_profesor = {
        'Nombre': nombre,
        'Edad': int(edad),
        'ID': identificacion,
        'Asignatura': asignatura
    }
    
    datos.profesores.append(nuevo_profesor)
    datos.guardar_datos()
    print("REGISTRADO EXITOSAMENTE")
    input("Presione Enter para continuar...")

def despredir_profesor():
    """Elimina un profesor del sistema (nombre original preservado)"""
    limpiar_pantalla()
    identificacion = input("Ingrese el numero de indentificación del profesor que desea despedir: ")

    for i, profesor in enumerate(datos.profesores):
        if profesor['ID'] == identificacion:
            datos.profesores.pop(i)
            datos.guardar_datos()
            print("Profesor despedido exitosamente.")
            input("Presione Enter para continuar...")
            return

    print("Profesor no encontrado.")
    input("Presione Enter para continuar...")

def actualizar_profesor():
    """Actualiza los datos de un profesor"""
    limpiar_pantalla()
    identificacion = input("Ingrese el numero de indentificación del profesor que desea actualizar: ")
    
    for profesor in datos.profesores:
        if profesor['ID'] == identificacion:
            print("Ingrese los nuevos datos del profesor:")
            nuevo_nombre = input("Ingrese el nuevo nombre del profesor: ")
            nueva_edad = input("Ingrese la nueva edad del profesor: ")
            nueva_id = input("Ingrese el nuevo número de identificación: ")
            nueva_asignatura = input("Ingrese la nueva asignatura: ")
            
            profesor['Nombre'] = nuevo_nombre
            profesor['Edad'] = int(nueva_edad)
            profesor['ID'] = nueva_id
            profesor['Asignatura'] = nueva_asignatura
            
            datos.guardar_datos()
            print("Profesor actualizado exitosamente.")
            input("Presione Enter para continuar...")
            return
    
    print("Profesor no encontrado.")
    input("Presione Enter para continuar...")