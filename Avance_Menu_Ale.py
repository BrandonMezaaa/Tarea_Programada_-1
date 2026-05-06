#Avance #1 Alejandro Madrigal y Brandon Meza Tarea Programada #1

"""Hoy miercoles 6 de mayo implemente la funcion mostrar tokens (Brandon Meza)"""
#Brandon no puede acceder al drive por lo que no a podido subir su avance




#=========================================================

tokens = []

#=========================================================

#Menú que se despliega al iniciar el programa para que el usuario sepa cual opcion debe ingresar
def menu():
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

        #La variable "opcion" guarda el numero str que seleccionó el usuario
        opcion = input("\nSeleccione una opcion: ")

        #Toma cada opcion posible y abre la funcion que corresponde
        if opcion == "1":
            cargar_tokens()
        elif opcion == "2":
            mostrar_tokens()
        elif opcion == "3":
            agregar_modificar_tokens()
        elif opcion == "4":
            guardar_tokens()
        elif opcion == "5":
            traducir_codigo()
        elif opcion == "6":
            generar_csv()
        elif opcion == "7":
            generar_html()
        elif opcion == "8":
            menu_bitacora()
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")
            
#========================================================
#Submenu que se encarga de la bitacora, abre la funcion de la opción que selecionó el usuario.
def menu_bitacora():
    while True:
        print("\nA. Acciones por dia escogido")
        print("B. Acciones con palabras clave")
        print("C. Salir del submenu")
 
        opcion = input("\nSeleccione una opcion: ").upper()
 
        if opcion == "A":
            filtrar_por_dia()
        elif opcion == "B":
            filtrar_por_palabra()
        elif opcion == "C":
            break
        else:
            print("Opcion invalida.")
#===========================================================
 
# Lee un archivo de tokens y los carga en la lista global.
# Si un token ya existe, lo sobreescribe con el nuevo valor.
def cargar_tokens():
    print("\n¿Como debe ser el archivo?")
    print("- Debe ser un archivo .txt")
    print("- Cada token debe estar en una linea separada")
    print("- Cada linea debe tener el formato: palabra separador reemplazo")
    print("- Ejemplo con '->' :    def -> funcion")
    print("- Ejemplo con ',' :    def, funcion")
    print("- Ejemplo con '=' :    def=funcion")
    print("- El archivo debe estar en la misma carpeta que el programa\n")
 
    nombre_archivo = input("Ingrese el nombre del archivo (ej: tokens.txt): ").strip()
    separador = input("Ingrese el separador usado en el archivo (ej: ->, ,, =): ").strip()
 
    archivo = open(nombre_archivo, "r")
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
 
        token_existente = False
        for i in range(len(tokens)):
            if tokens[i][0] == palabra:
                print(f"Token '{palabra}' reescrito: '{tokens[i][1]}' -> '{reemplazo}'")
                tokens[i] = (palabra, reemplazo)
                token_existente = True
                break
 
        if not token_existente:
            tokens.append((palabra, reemplazo))
            print(f"Token '{palabra}' agregado.")
 
    print(f"\nTokens cargados exitosamente desde '{nombre_archivo}'.")
 
#=========================================================
# Muestra todos los tokens actualmente cargados en memoria
def mostrar_tokens():
    if len(tokens) == 0:
        print("\nNo hay tokens cargados.")
        return
 
    print("\nTokens cargados:")
    for i in range(len(tokens)):
        print(f"{tokens[i][0]} -> {tokens[i][1]}")
 
def agregar_modificar_tokens():
    pass
 
def guardar_tokens():
    pass
 
def traducir_codigo():
    pass
 
def generar_csv():
    pass
 
def generar_html():
    pass
 
def filtrar_por_dia():
    pass
 
def filtrar_por_palabra():
    pass
 
 
menu()
