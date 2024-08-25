##Creaando funciones del menu
def crea_usuario():
    """comentario sobre la funcion"""
    print("opcion 1")
    
def crea_paquete_turistico():
    """"comentario sobre la funcion"""
    print("opcion 2")
    
def busca_paquete_turistico():
    """comentario sobre la funcion"""
    print("opcion 3")
    
def reservar_vuelo():
    """comentario sobre la funcion"""
    print("opcion 4")
def reservar_hotel():
    """comentario sobre la funcion"""
    print("opcion 5")

##Creando diccionario con las diferentes opciones
menu_opciones = {
    '1':crea_usuario,
    '2':crea_paquete_turistico,
    '3':busca_paquete_turistico,
    '4':reservar_vuelo,
    '5':reservar_hotel
} 
##Inicializando variables
salir = False
mensaje_bienvenida = "Bienvenido al menu de la Agencia"

##Creando bucle para repetir el menu 
while not salir:
    print("*"*len(mensaje_bienvenida))
    print(mensaje_bienvenida)
    print("*"*len(mensaje_bienvenida))
    #Mostrando opciones del menu en cosola
    print("\n 1.Crear usuario")
    print(" 2.Crear paquete turistico")
    print(" 3.Buscar paquetes turisticos")
    print(" 4.Reservar vuelos")
    print(" 5.Reservar hotel")
    print(" 6.Salir")
    #Solicitando opcion al usuario
    opcion = input("\n Ingresa una opcion: ")
    #Invocando funcion escogida por el usuario
    if opcion in menu_opciones:
        menu_opciones[opcion]()
    #Saliendo del menu      
    elif opcion == '6':
        print("***Gracias por usar nuestro servicio***")
        salir = True
    #Mensaje en caso de que se ingrese un dato equivocado
    else:
        print("\n***Ingresa una opcion valida***\n")