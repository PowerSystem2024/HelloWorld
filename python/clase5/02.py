# hacer un programa que simule una agenda de contactos, crear un diccionario
# donde la clase sea el nombre del usuario y el valor sea el teelefono, el programa debe tener el sgte menu:

# nuevo contacto
# borrar contacto
# ver contactos existentes
# salir

def agendaTelefonica():

    agenda = {
        "pepe": 2604352412,
        "alberto": 2604310989,
        "miriam": 260431234
    }

    while True:

        opcion = int(input("""A continuación, seleccione una opción: \n
                    1 - Crear un nuevo contacto
                    2 - Eliminar un contacto
                    3 - Ver contactos existentes
                    4 - Salir \n
                    """))

        if opcion == 1:

            nombre = input("Ingrese el nombre para el nuevo contacto: ")
            numero = int(input(f"Ingrese el número para el contacto {nombre}: "))

            agenda[nombre] = numero
            print(f"Contacto {nombre} agregado correctamente.\n")

        elif opcion == 2:

            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")

            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado correctamente.\n")
            else:
                print(f"El contacto {nombre} no existe en la agenda.\n")

        elif opcion == 3:

            print("Contactos existentes:")
            for nombre, numero in agenda.items():
                print(f"{nombre}: {numero}")
            print()

        elif opcion == 4:
            print("Saliendo de la agenda.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.\n")

agendaTelefonica()
