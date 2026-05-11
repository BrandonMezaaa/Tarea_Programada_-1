#Elaborado por: Alejandro Madrigal y Brandon Meza
# Fecha de creacion: 06/05/2026
# Ultima modificacion: 11/05/2026
# Version de Python: 3.11
"""Ale :D
Hoy lunes terminaré todas las funciones posibles para que solo falte completar la documentación"""
#=========================================================

tokens = []

#=========================================================

def menu():
    """
    Funcionalidad: Despliega el menu principal del programa y redirige
                   al usuario a la funcion correspondiente segun su eleccion
    Entradas: Ninguna
    Salidas: Ninguna
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
            print("Opcion invalida")

#=========================================================

def menuBitacora():
    """
    Funcionalidad: Despliega el submenu de bitacora y redirige al usuario
                   a la funcion correspondiente segun su eleccion
    Entradas: Ninguna
    Salidas: Ninguna
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
            print("Opcion invalida")

#=========================================================

def cargarTokens():
    """
    Funcionalidad: Lee un archivo .txt con tokens y los carga en la lista
                   global. Si un token ya existe lo sobreescribe con el nuevo valor
    Entradas:
        - nombreArchivo(str): Nombre del archivo .txt ingresado por el usuario.
        - separador(str): Caracter separador usado en el archivo (ej: ->, ,, =)
    Salidas: Modifica la lista global tokens directamente
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
    Funcionalidad: Muestra todos los tokens actualmente cargados en memoria
    Entradas: Ninguna
    Salidas: Imprime los tokens en consola
    """
    if len(tokens) == 0:
        print("\nNo hay tokens cargados.")
        return

    print("\nTokens cargados:")
    for i in range(len(tokens)):
        print(f"{tokens[i][0]} -> {tokens[i][1]}")

#=========================================================
def agregarModificarTokens():
    """
    Funcionalidad: Pide los separadores y recibe una cadena con la modificación o con los nuevos tokens y los carga en la lista
                   global. Si un token ya existe lo sobreescribe con el nuevo valor y indica al usuario el cambio realizado.
    Entradas:
        - separador(str): Caracter separador usado en el archivo (ej: ->, ,, =).
        - separaToken: Caracter separador pero entre Tokens, usado para que el usuario dijite todo en una cadena larga como se solicita
        - cadenaUsuario: Es la cadena que ingresa el usuario y que se usa para tomar los nuevos tokens
        - decision: Se muestra lo ingresado al usuario y se le pregunta si desea continuar...
    Salidas: Ninguna. Modifica la lista global tokens directamente.

    """
    
    print("\n¿Como debe ingresar los tokens?")
    print("- Cada Token debe tener el formato: palabra separador reemplazo caracterFin")
    print("- Ejemplo si el separador es '='")
    print("- Y el caracter final usado para separar los tokens es ','")
    print("- Debe verse así: return = devuelva , print = pinte , def = función , while = mientras")
    print("- Si al final desea realizar el cambio ingrese 'aceptar', de lo contrario ingrese 'cancelar' \n")

    separador=input("\nIngrese el separador que va a utilizar para los Tokens: ")
    separadorToken=input("\nIngrese el caracter final que va a utilizar entre Tokens: ")
    cadenaUsuario=input("Ingrese la cadena con los token a ingresar: ")
    
    #Divide el texto ingresado por el usuario usando un separador específico (split) y elimina los espacios sobrantes de cada elemento (strip), guardando el resultado en una lista.
    lineas = [i.strip() for i in cadenaUsuario.split(separadorToken)]
    print("\nCadena recibida:\n",lineas)

    
    decision = input("\n¿Desea continuar con la modificación? (aceptar/cancelar): ").lower()
    if decision == "cancelar":
        print("\nOperación cancelada.")
        return

    elif decision != "aceptar":
        print("\nOpción inválida.")
        return

    
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

    print("\nTokens cargados exitosamente")

#=========================================================

def guardarTokens():
    """
    Funcionalidad: Guarda los tokens actualmente en memoria en un archivo .txt nuevo
    Entradas:
        - nombreArchivo(str): Nombre del archivo donde se van a guardar los tokens
        - separador(str): Caracter separador que se usara para guardar los tokens
    Salidas: Crea un archivo .txt con los tokens en la carpeta del programa
    """
    if len(tokens) == 0:
        print("\nNo hay tokens cargados para guardar")
        return

    nombreArchivo = input("Ingrese el nombre del archivo a guardar (ej: tokens.txt): ").strip()
    separador = input("Ingrese el separador que desea usar (ej: ->, ,, =): ").strip()

    archivo = open(nombreArchivo, "w")
    for i in range(len(tokens)):
        archivo.write(f"{tokens[i][0]} {separador} {tokens[i][1]}\n")
    archivo.close()

    print(f"\nTokens guardados exitosamente en '{nombreArchivo}'")

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
