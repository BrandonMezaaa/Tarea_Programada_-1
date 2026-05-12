#Elaborado por: Alejandro Madrigal y Brandon Meza
# Fecha de creacion: 06/05/2026
# Ultima modificacion: 11/05/2026
# Version de Python: 3.11
"""Ale :D
Hoy lunes terminaré todas las funciones posibles para que solo falte completar la documentación"""
#=========================================================
import re
from datetime import datetime
#========================================================
#!!!!!!!!!!!!!!Tokens de prueba, quitar al final dejar []
tokens = [('return', 'devuelva'), ('print', 'pinte'), ('def', 'funciÃ³n'), ('while', 'mientras')]
conteoTokens =[]
totalPalabras =0
relog=0
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

    try:
        archivo = open(nombreArchivo, "r")
    except:
        print("\nEl archivo no existe, intentelo de nuevo con el formato nombre.txt o nombre.py y asegurese de que se encuentre en la misma carpeta que este programa.")
        return
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

#==========================================================================================================

def traducirCodigo():
    """
    Utilidad: Toma un archivo dado por el usuario, pregunta por el nombre del nuevo archivo a crear,
    luego toma el codigo recibido, lo lee linea por linea, las separa con ayuda de las expresiones regulares y listas
    y toma las palabras que encuentra identicas a las que hay en el archivo de tokens y los va reemplazando.
    Además va generando los distintos reportes de rendimiento y procesos simultaneamente

    Entradas:
    - nombreArchivo(str): Nombre del archivo .txt o .py ingresado por el usuario que se va a traducir.
    - nombreArchSalida(str):Nombre del archivo que se usa para guardar el texto/código traducido.
    Salidas:
    - nuevoArchivo: Archivo traducido
    """
    cadenaFin=""
    global conteoTokens
    global totalPalabras
    global relog
    for palabra, reemplazo in tokens:
        conteoTokens += [(palabra, reemplazo, 0)]

    
    nombreArchivo = input("Ingrese el nombre del archivo (ej: codigo.py): ").strip()
    nombreArchSalida = input("Ingrese el nombre para el nuevo archivo ya traducido (nombre.py/txt): ").strip()

    relog = datetime.now().timestamp()

    if not re.match(r"\w+[.](txt|py)", nombreArchSalida): #w Uno o mas alfanumerico. "." txt o py
        print("\nNombre de archivo inválido.")
        return

    try:
        archivo = open(nombreArchivo, "r")
    except:
        print("\nEl archivo no existe, intentelo de nuevo con el formato nombre.txt o nombre.py y asegurese de que se encuentre en la misma carpeta que este programa.")
        return
    lineas = archivo.readlines()
    archivo.close()
    
    
    for linea in lineas:
        
        #Expresion regular: \w+ uno o más caracteres alfanumericos
        #| funciona como or. []=Grupo de caracteres. \s+ guarda los espacios en blanco originales
        # ^ negado. \caracteres alfanumericos y \s espacios en blanco
        partes = re.findall(r'\w+|\s+|[^\w\s]', linea)

        nuevaLinea =""
        contador=0
        for parte in partes:

            if re.match(r'\w+', parte):
                totalPalabras += 1

            for i in range(len(tokens)):

                if tokens[i][0] == parte:
                    partes[contador] = tokens[i][1]

                    conteoTokens[i] = (conteoTokens[i][0], conteoTokens[i][1], conteoTokens[i][2] + 1)

            nuevaLinea += partes[contador]
            contador += 1

        cadenaFin += nuevaLinea

    try:
        archivoPrueba = open(nombreArchSalida, "r")
        archivoPrueba.close()
        print("\nEl archivo ya existe, será modificado.")

    except:
        print("\nEl archivo no existe, se creará uno nuevo.")

    nuevoArchivo = open(nombreArchSalida, "w")
    nuevoArchivo.write(cadenaFin)
    nuevoArchivo.close()

    print("\nArchivo traducido exitosamente.")
    relog = datetime.now().timestamp() - relog
    relog = round(relog, 2)
#==================================================================================================
        
def generarCsv():
    """
    Utilidad: Funcion que trabaja mediante un contador
    que aumenta cada vez que el programa encuentre una palabra que sí está en la lista tokens,
    aumenta en 1 el contador de esa palabra. Y genera un CSV con el nombre que el usuario indique
    Entradas:
    - nombreArchivo(str): Nombre del archivo que el usuario desea dar al reporte CSV.
    Salidas:
    - nuevoArchivo: Archivo CSV con el reporte
    """
    
    nombreArchivo = input("Ingrese el nombre que desea para crear/reescribir el reporte CSV \nEjemplo 'reporte1': ").strip() + ".csv"
    archivo = open(nombreArchivo, "w")

    archivo.write("sep=;\n")
    archivo.write("Original;Reemplazo;Cantidad\n")

    for token in conteoTokens:
        archivo.write(f"{token[0]};{token[1]};{token[2]}\n")
    archivo.close()

    print("\nReporte CSV generado exitosamente.")


#==================================================================================================

def generarHtml():
    """
    Utilidad: Funcion que crea un reporte en html que indica:
    Duración total del procesamiento, cantidad total de reemplazos y porcentaje de palabras reemplazadas
    ademas de registrar la fecha de cada reporte de html
    Entradas: 
    - tituloReporte(str): Es el título que lleva el HTML en la pestaña donde está abierto.
    Salidas:
    - archivo .html: Archivo html con el reporte
    """

    tituloReporte=input("Ingrese el que desea mostrar en la pestaña donde se abra: ")

    #Suma del total de remplazos hechos.
    totalReemplazos=0
    for token in conteoTokens:
        totalReemplazos+=token[2]

    #Porcentaje de palabras reemplazadas, evito dividir 0
    try:
        porcentajePR= (totalReemplazos / totalPalabras) *100
    except:
        porcentajePR=0
        
    #Creación del html
    fechaActual=datetime.now()
    fechaActual=fechaActual.strftime("%d-%m-%y_%H-%M-%S")#Da formato a la fecha
    nombreArchivo="reporteHTML_"+fechaActual+".html"
    archivo = open(nombreArchivo, "w", encoding="utf-8")
    archivo.write("<html>\n")

    #Modificacion de la pestaña
    archivo.write("<head>\n")
    archivo.write("<title>" + tituloReporte + "</title>\n")
    archivo.write("</head>\n")

    #Cuerpo del html
    archivo.write("<body>\n")
    archivo.write("<h1>Reporte de Traducción</h1>\n")
    archivo.write("<h2>Fecha y hora de generación: " + fechaActual + "</h2>\n")

    archivo.write("<p>Duración total del procesamiento: " + str(relog) + " segundos</p>\n")
    archivo.write("<p>Cantidad total de reemplazos: " + str(totalReemplazos) + "</p>\n")
    archivo.write("<p>Porcentaje de palabras reemplazadas: " + str(porcentajePR) + "%</p>\n")
    
    #Creacion de la tabla
    archivo.write("<table border='1' style='border-collapse: collapse;'>\n")

    archivo.write("<tr>\n") #Crea Fila
    #Encabezados
    archivo.write("<th>Palabra original</th>\n")
    archivo.write("<th>Reemplazo</th>\n")
    archivo.write("<th>Cantidad de reemplazos</th>\n")
    #Fila
    archivo.write("</tr>\n")

    for i in range(len(conteoTokens)):
        token = conteoTokens[i]

        if i % 2 == 0:#Si la fila es par, pinta blanco, sino gris
            color = "white"
        else:
            color = "lightgray"

        archivo.write("<tr style='background-color:" + color + "; text-align:center;'>\n") #Da formato a la fila
        archivo.write("<td>" + token[0] + "</td>\n")#Agrega las 3 partes de la fila
        archivo.write("<td>" + token[1] + "</td>\n")
        archivo.write("<td>" + str(token[2]) + "</td>\n")
        archivo.write("</tr>\n")#Fila nueva y repite



#Cerrado de Html
    archivo.write("</table>\n")
    archivo.write("</body>\n")
    archivo.write("</html>\n")
    archivo.close()

    print("Reporte HTML generado:", nombreArchivo)
    

def filtrarPorDia():
    pass

def filtrarPorPalabra():
    pass


menu()
