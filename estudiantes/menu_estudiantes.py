import os
import json
from estudiantes.estudiantes import datos

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_grados(titulo="Elija el grado en el cual desea matricular:"):
    """Muestra el menú de grados"""
    limpiar_pantalla()
    print(titulo)
    print("1- Grado 6")
    print("2- Grado 7")
    print("3- Grado 8")
    print("4- Grado 9")
    print("5- Grado 10")
    print("6- Grado 11")
    print("0- Atras")

def obtener_nombre_grado(opcion):
    """Convierte el número de opción al nombre del grado"""
    grados = {
        "1": "SEXTO",
        "2": "SEPTIMO",
        "3": "OCTAVO",
        "4": "NOVENO",
        "5": "DECIMO",
        "6": "UNDECIMO"
    }
    return grados.get(opcion, "")

def ver_estudiantes():
    """Muestra la lista de estudiantes por grado"""
    while True:
        mostrar_menu_grados("Elija la lista del grado que desea visualizar:")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "0":
            break
        
        grado = obtener_nombre_grado(opcion)
        if grado:
            limpiar_pantalla()
            print(f"Lista de estudiantes matriculados en el grado {grado}")
            estudiantes_grado = [e for e in datos.estudiantes if e['grado'] == grado]
            
            if estudiantes_grado:
                for estudiante in estudiantes_grado:
                    print(estudiante)
            else:
                print("No hay estudiantes matriculados en este grado.")
            
            input("\nPresione Enter para continuar...")
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")

def matricular_estudiante():
    """Matricula un nuevo estudiante"""
    while True:
        mostrar_menu_grados()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "0":
            break
        
        grado = obtener_nombre_grado(opcion)
        if grado:
            limpiar_pantalla()
            print("Ingrese los datos requeridos")
            nombre = input("Ingrese nombre: ")
            edad = input("Ingrese Edad: ")
            identificacion = input("Ingrese su numero de identificacion: ")
            
            nuevo_estudiante = {
                'Nombre': nombre,
                'Edad': int(edad),
                'ID': identificacion,
                'grado': grado
            }
            
            datos.estudiantes.append(nuevo_estudiante)
            datos.guardar_datos()
            print("REGISTRADO EXITOSAMENTE")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")

def expulsar_estudiante():
    """Elimina un estudiante del sistema"""
    while True:
        mostrar_menu_grados("Elija el grado del estudiante que desea expulsar:")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "0":
            break
        
        grado = obtener_nombre_grado(opcion)
        if grado:
            limpiar_pantalla()
            identificacion = input("Ingrese el numero de indentificación del estudiante que desea expulsar: ")
            
            for i, estudiante in enumerate(datos.estudiantes):
                if estudiante['ID'] == identificacion and estudiante['grado'] == grado:
                    estudiante_eliminado = estudiante.copy()
                    del estudiante_eliminado['grado']
                    datos.estudiantes.pop(i)
                    datos.guardar_datos()
                    print(f"Estudiante eliminado exitosamente: {estudiante_eliminado}")
                    input("Presione Enter para continuar...")
                    return
            
            print("Estudiante no encontrado en este grado.")
            input("Presione Enter para continuar...")
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")

def actualizar_estudiante():
    """Actualiza los datos de un estudiante"""
    while True:
        mostrar_menu_grados("Elija el grado del estudiante que desea actualizar datos:")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "0":
            break
        
        grado = obtener_nombre_grado(opcion)
        if grado:
            limpiar_pantalla()
            identificacion = input("Ingrese el numero de indentificación del estudiante al cual se le actualizara los datos: ")
            
            for estudiante in datos.estudiantes:
                if estudiante['ID'] == identificacion and estudiante['grado'] == grado:
                    nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
                    nueva_edad = input("Ingrese la nueva edad del estudiante: ")
                    nueva_id = input("Ingrese el nuevo numero de indentificación del estudiante: ")
                    
                    estudiante['Nombre'] = nuevo_nombre
                    estudiante['Edad'] = int(nueva_edad)
                    estudiante['ID'] = nueva_id
                    
                    datos.guardar_datos()
                    print("Estudiante modificado exitosamente.")
                    input("Presione Enter para continuar...")
                    return
            
            print("Estudiante no encontrado en este grado.")
            input("Presione Enter para continuar...")
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")