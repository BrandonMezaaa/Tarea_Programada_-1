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
 
        opcion = input("\nSeleccione una opcion: ")
 
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
 
 
def cargar_tokens():
    pass
 
def mostrar_tokens():
    pass
 
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