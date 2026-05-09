# Elaborado por: Alejandro Madrigal y Brandon Meza
# Fecha de creacion: 28/04/2026
# Ultima modificacion: 09/05/2026
# Version de Python: 3.11

"""
Hoy converti todo el proyecto a codigo camello y lo documente de la manera de la cual se me fue indicada (Brandon Meza)
"""

#=========================================================

tokens = []

#=========================================================

def menu():
    """
    Funcionalidad: Despliega el menu principal del programa y redirige
                   al usuario a la funcion correspondiente segun su eleccion.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    while True:
        print("\n1. Cargar tokens")
        print("2. Mostrar tokens")
        print("3. Agregar/Modificar token")
        print("4. Guardar tokens")
        print("5. Traducir codigo")
        print("6. Generar CSV")
        print("7. Generar HTML")
        print("8. Bitacora del sistema")
        print("9. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            cargarTokens()
        elif opcion == "2":
            mostrarTokens()
        elif opcion == "3":
            agregarModificarTokens()
        elif opcion == "4":
            guardarTokens()
        elif opcion == "5":
            traducirCodigo()
        elif opcion == "6":
            generarCsv()
        elif opcion == "7":
            generarHtml()
        elif opcion == "8":
            menuBitacora()
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")

#=========================================================

def menuBitacora():
    """
    Funcionalidad: Despliega el submenu de bitacora y redirige al usuario
                   a la funcion correspondiente segun su eleccion.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    while True:
        print("\nA. Acciones por dia escogido")
        print("B. Acciones con palabras clave")
        print("C. Salir del submenu")

        opcion = input("\nSeleccione una opcion: ").upper()

        if opcion == "A":
            filtrarPorDia()
        elif opcion == "B":
            filtrarPorPalabra()
        elif opcion == "C":
            break
        else:
            print("Opcion invalida.")

#=========================================================

def cargarTokens():
    """
    Funcionalidad: Lee un archivo .txt con tokens y los carga en la lista
                   global. Si un token ya existe lo sobreescribe con el nuevo valor.
    Entradas:
        - nombreArchivo(str): Nombre del archivo .txt ingresado por el usuario.
        - separador(str): Caracter separador usado en el archivo (ej: ->, ,, =).
    Salidas: Ninguna. Modifica la lista global tokens directamente.
    """
    print("\n¿Como debe ser el archivo?")
    print("- Debe ser un archivo .txt")
    print("- Cada token debe estar en una linea separada")
    print("- Cada linea debe tener el formato: palabra separador reemplazo")
    print("- Ejemplo con '->' :    def -> funcion")
    print("- Ejemplo con ',' :    def, funcion")
    print("- Ejemplo con '=' :    def=funcion")
    print("- El archivo debe estar en la misma carpeta que el programa\n")

    nombreArchivo = input("Ingrese el nombre del archivo (ej: tokens.txt): ").strip()
    separador = input("Ingrese el separador usado en el archivo (ej: ->, ,, =): ").strip()

    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        linea = linea.strip()

        if linea == "":
            continue

        partes = linea.split(separador)

        if len(partes) != 2:
            print(f"Linea con formato incorrecto, se omite: '{linea}'")
            continue

        palabra = partes[0].strip()
        reemplazo = partes[1].strip()

        tokenExistente = False
        for i in range(len(tokens)):
            if tokens[i][0] == palabra:
                print(f"Token '{palabra}' reescrito: '{tokens[i][1]}' -> '{reemplazo}'")
                tokens[i] = (palabra, reemplazo)
                tokenExistente = True
                break

        if not tokenExistente:
            tokens.append((palabra, reemplazo))
            print(f"Token '{palabra}' agregado.")

    print(f"\nTokens cargados exitosamente desde '{nombreArchivo}'.")

#=========================================================

def mostrarTokens():
    """
    Funcionalidad: Muestra todos los tokens actualmente cargados en memoria.
    Entradas: Ninguna.
    Salidas: Ninguna. Imprime los tokens en consola.
    """
    if len(tokens) == 0:
        print("\nNo hay tokens cargados.")
        return

    print("\nTokens cargados:")
    for i in range(len(tokens)):
        print(f"{tokens[i][0]} -> {tokens[i][1]}")

#=========================================================

def agregarModificarTokens():
    pass

def guardarTokens():
    pass

def traducirCodigo():
    pass

def generarCsv():
    pass

def generarHtml():
    pass

def filtrarPorDia():
    pass

def filtrarPorPalabra():
    pass


menu()
