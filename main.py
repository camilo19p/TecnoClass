import os
import json
from estudiantes import menu_estudiantes
from profesores import menu_profesores

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    limpiar_pantalla()
    print("Menu Principal:")
    print("1- Ver Estudiantes matriculados")
    print("2- Ver profesores registrados en la institucion")
    print("3- Matricular estudiante")
    print("4- registro de profesores")
    print("5- Expulsar Estudiante")
    print("6- Actualizar datos del estudiante")
    print("7- Despedir profesor")
    print("8- Actualizar datos del profesor")
    print("0- Salir")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            menu_estudiantes.ver_estudiantes()
        elif opcion == "2":
            menu_profesores.ver_profesores()
        elif opcion == "3":
            menu_estudiantes.matricular_estudiante()
        elif opcion == "4":
            menu_profesores.registrar_profesor()
        elif opcion == "5":
            menu_estudiantes.expulsar_estudiante()
        elif opcion == "6":
            menu_estudiantes.actualizar_estudiante()
        elif opcion == "7":
            menu_profesores.despredir_profesor()
        elif opcion == "8":
            menu_profesores.actualizar_profesor()
        elif opcion == "0":
            limpiar_pantalla()
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()