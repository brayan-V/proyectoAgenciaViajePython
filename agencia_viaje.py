vuelos = {
    1: {"Ciudad": "Bogota", "salidas": {"a": 130.000, "b": 140.000, "c": 150.000}},
    2: {"Ciudad": "Medellin", "salidas": {"a": 145.000, "b": 155.000, "c": 165.000}},
    3: {"Ciudad": "Santa Marta", "salidas": {"a": 160.000, "b": 170.000,  "c": 180.000}},
    4: {"Ciudad": "Amazonas", "salidas": {"a": 175.000, "b": 185.000, "c": 200.000}}
}

hoteles = {
    1: {
        1:{"Nombre": "Hotel arena suites 4 dias - 3 noches", "Tours": "La Candelaria, Monserrate y Museo del Oro Bogotá City Tour", "precio": 643.000 },
        2: {"Nombre": "Hotel Radisson Bogota Metrotel 4 dias - 3 noches", "Tours": "Bogota Tour Privado Catedral de Sal Zipaquira + Almuerzo", "precio": 999.999},
        3: {"Nombre": "Hotel Radel Bogotá  3 dias - 2 noches", "Tours": "Tour gastronómico por el Viejo Bogotá con más de 12 degustaciones", "precio": 415.000  }
    },
    2: {
        1:{"Nombre": "Hotel Sie7e 4 dias - 3 noches", "Tours": "Tour a Guatape, Piedra del Peñol con Recorrido en Barco, Desayuno y Almuerzo", "precio": 570.000},
        2:{"Nombre": "Hotel Med Laureles 3 dias - 2 noches", "Tours": "City tour Medellin + Comuna 13 + Graffititour Se paisa por un dia", "precio": 572.000 },
        3:{"Nombre": "Stanza Hotel Medellin 4 dias - 3 noches", "Tours": "Excursión a plantación de café y paseo a caballo: Todo en un gran e inolvidable día", "precio": 999.999}
    },
    3: {
        1:{"Nombre": "Hotel Boutique ADAZ 4 dias - 3 noches", "Tours": "Tour de Día Completo en Catamarán por el Tayrona", "precio": 755.000},
        2:{"Nombre": "Titanic Hotel 3 dias - 2 noches", "Tours": "Parque Tayrona - Cabo San Juan", "precio": 395.000},
        3:{"Nombre": "Hotel Carolina Del Mar 4 dias - 3 noches", "Tour": "Tour Privado Piedras de Donama en Sierra Nevada de Santa Marta", "precio": 999.999}
    },
    4: {
        1:{"Nombre": "Hostel Casa de las Palmas 4 dias - 3 noches", "Tours": "Visita Puerto Nariño, Tres Fronteras y la Reserva Marasha ", "precio": 845.000},
        2:{"Nombre": "Hotel Yurupary 3 dias - 2 noches", "Tours": "Visita la reserva Natural Kindiwaira y la cascada fin del Mundo en Putumayo", "precio": 850.000 }
    }
}

import time
##Fución para validar que la entrada sea un numero entero
def validar_entrada(mensaje):
    entrada = input(mensaje)
    if entrada.isdigit():##.isdigit verifica si la cadena es un numero
        return int(entrada)##Retornamos la entrada 
    else:
        print("Ingresa un valor numerico")
        return validar_entrada(mensaje)##En caso que la entra sea algo diferente a un numero volvemos a llamar la funcion    
##Creando funciones del menu

def crea_usuario():
    """Función que solicita los datos del usuario y 
    lo agrega al diccionario de usuarios"""
    print("\033c", end="") ##Limpiar consola
    id_usuario = validar_entrada("Ingresa la identificacion del usuario: ")
    #Validando que no hayan identificiones duplicadas
    if id_usuario in diccionario_usuarios:
        print("***Identificacion en uso, ingresa una nueva.***")
        time.sleep(1)
        return crea_usuario()
    nombre = input("Ingresa el nombre del usuario: ")
    apellido = input("Ingresa el apellido del usuario: ")
    edad = validar_entrada("Ingresa la edad del usuario: ")
    #Creando diccionario para el  usuario
    usuario ={'nombre': nombre,'apellido': apellido,'edad': edad}
    """Agregando al usuario al diccionario de usuarios, usando
    el id_usuario como clave"""    
    diccionario_usuarios[id_usuario]=usuario
    print(f"***Usuario {nombre} {apellido} Creado con exito***")

def eliminar_usuario():
    """"Función para eliminar a un usuario usando su Id 
        para buscarlo en el diccionario"""
    print("\033c", end="")##Limpiar consola
    identificacion = validar_entrada("Ingresa la identificacion del clientes que deseas eliminar: ")
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
    if len(diccionario_usuarios) == 0:##Validando si el diccionario esta vacio
        print("***No hay usuarios registrados***")
    else:
        for id, usuario in diccionario_usuarios.items():
            print(f"ID:{id} {usuario['nombre']} {usuario['apellido']} {usuario['edad']} años")
            print("-"*25)
        
def crea_paquete_turistico():
    """"comentario sobre la funcion"""
    print("\033c", end="")## Limpiar consola

def busca_paquete_turistico():
    """comentario sobre la funcion"""
    print("opcion 3")
    
def reservar_vuelo():
    """comentario sobre la funcion"""
    print("opcion 4")
def reservar_hotel():
    """comentario sobre la funcion"""
    print("opcion 5")

def mostrar_compra():
    """comentario sobre la funcion"""

##Creando diccionario con las diferentes opciones
menu_opciones = {
    '1':crea_usuario,
    '2':eliminar_usuario,
    '3':mostrar_usuarios,
    '4':crea_paquete_turistico,
    '5':busca_paquete_turistico,
    '6':reservar_vuelo,
    '7':reservar_hotel,
    '8':mostrar_compra
}

##Creando diccionario vacio para almacenar a los usuarios
diccionario_usuarios ={} 
##Inicializando variables
mensaje_bienvenida = "Bienvenido al menu de la Agencia"
##Creando bucle para repetir el menu 
while True:
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
    print(" 8.Resumen de la compra")
    print(" 9.Salir")
    #Solicitando opcion al usuario
    opcion = input("\n Ingresa una opcion: ")
    #Invocando Fución escogida por el usuario
    if opcion in menu_opciones:
        menu_opciones[opcion]()
    #Saliendo del menu      
    elif opcion == '9':
        print("***Gracias por usar nuestro servicio***")
        break
    #Mensaje en caso de que se ingrese un dato equivocado
    else:
        print("\n***Ingresa una opcion valida***\n")
