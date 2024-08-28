##Creando funciones del menu

def crea_usuario():
    """Función que solicita los datos del usuario y 
    lo agrega a la lista de usuarios"""
    print("\033c", end="") ##Limpiar consola
    id_usuario = int(input("Ingresa la identificacion del usuario: "))
    nombre = input("Ingresa el nombre del usuario: ")
    apellido = input("Ingresa el apellido del usuario: ")
    edad = int(input("Ingresa la edad del usuario: "))
    #Validando que no hayan identificiones duplicadas
    if id_usuario in diccionario_usuarios:
        print("***Identificacion en uso , ingresa un nueva.***")
        return
    #Creando diccionario para el  usuario
    usuario ={
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
    }
    """Agregando al usuario al diccionario de usuarios, usando
    el id_usuario como clave"""    
    diccionario_usuarios[id_usuario]=usuario
    print(f"***Usuario {nombre} {apellido} Creado con exito***")
        
def eliminar_usuario():
    """"Función para eliminar a un usuario usando su Id 
        para buscarlo en el diccionario"""
    print("\033c", end="")##Limpiar consola
    identificacion = int(input(print("Ingresa la identificacion del clientes que deseas eliminar: ")))
    ##Validando que la identificacion exista en el diccionario
    if identificacion in diccionario_usuarios:
        ##Eliminando al usuario con la funcion pop 
        diccionario_usuarios.pop(identificacion)
        print("***El usuario fue eliminado con exito***")
    else:
        print("***La identificacion no existe***")
def mostrar_usuarios():
    """"Función que recorre nuestro diccionario de clientes e imprime en 
        pantalla sus datos."""
    print("\033c", end="")## Limpiar consola
    ##Recorriendo el diccionario, usando la función .items() que nos retorna la clave y el valor
    for id, usuario in diccionario_usuarios.items():
        print(f"ID:{id} {usuario['nombre']} {usuario['apellido']} {usuario['edad']} años")
        print("-"*25)
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
    '2':eliminar_usuario,
    '3':mostrar_usuarios,
    '4':crea_paquete_turistico,
    '5':busca_paquete_turistico,
    '6':reservar_vuelo,
    '7':reservar_hotel
}
##Creando diccionaria vacio para almacenar a los usuarios
diccionario_usuarios ={} 
##Inicializando variables
salir = False
mensaje_bienvenida = "Bienvenido al menu de la Agencia"

##Creando bucle para repetir el menu 
while not salir:
    print("*"*len(mensaje_bienvenida))
    print(mensaje_bienvenida)
    print("*"*len(mensaje_bienvenida))
    #Mostrando opciones del menu en consola
    print("\n 1.Crear usuario")
    print(" 2.Eliminar usuario")
    print(" 3.Mostrar usuarios")
    print(" 4.Crear paquete turistico")
    print(" 5.Buscar paquetes turisticos")
    print(" 6.Reservar vuelos")
    print(" 7.Reservar hotel")
    print(" 8.Salir")
    #Solicitando opcion al usuario
    opcion = input("\n Ingresa una opcion: ")
    #Invocando funcion escogida por el usuario
    if opcion in menu_opciones:
        menu_opciones[opcion]()
    #Saliendo del menu      
    elif opcion == '8':
        print("***Gracias por usar nuestro servicio***")
        salir = True
    #Mensaje en caso de que se ingrese un dato equivocado
    else:
        print("\n***Ingresa una opcion valida***\n")