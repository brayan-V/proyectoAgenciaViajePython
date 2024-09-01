vuelos = {
    1: {"Ciudad": "Bogota", "salidas": {"a": 130000, "b": 140000, "c": 150000}},
    2: {"Ciudad": "Medellin", "salidas": {"a": 145000, "b": 155000, "c": 165000}},
    3: {"Ciudad": "Santa Marta", "salidas": {"a": 160000, "b": 170000,  "c": 180000}},
    4: {"Ciudad": "Amazonas", "salidas": {"a": 175000, "b": 185000, "c": 200000}}
}

hoteles = {
    1: {
        1:{"Nombre": "Hotel arena suites 4 dias - 3 noches", "Tours": "La Candelaria, Monserrate y Museo del Oro Bogotá City Tour", "precio": 643000 },
        2: {"Nombre": "Hotel Radisson Bogota Metrotel 4 dias - 3 noches", "Tours": "Bogota Tour Privado Catedral de Sal Zipaquira + Almuerzo", "precio": 999999},
        3: {"Nombre": "Hotel Radel Bogotá  3 dias - 2 noches", "Tours": "Tour gastronómico por el Viejo Bogotá con más de 12 degustaciones", "precio": 415000  }
    },
    2: {
        1:{"Nombre": "Hotel Sie7e 4 dias - 3 noches", "Tours": "Tour a Guatape, Piedra del Peñol con Recorrido en Barco, Desayuno y Almuerzo", "precio": 570000},
        2:{"Nombre": "Hotel Med Laureles 3 dias - 2 noches", "Tours": "City tour Medellin + Comuna 13 + Graffititour Se paisa por un dia", "precio": 572000 },
        3:{"Nombre": "Stanza Hotel Medellin 4 dias - 3 noches", "Tours": "Excursión a plantación de café y paseo a caballo: Todo en un gran e inolvidable día", "precio": 999999}
    },
    3: {
        1:{"Nombre": "Hotel Boutique ADAZ 4 dias - 3 noches", "Tours": "Tour de Día Completo en Catamarán por el Tayrona", "precio": 755000},
        2:{"Nombre": "Titanic Hotel 3 dias - 2 noches", "Tours": "Parque Tayrona - Cabo San Juan", "precio": 395000},
        3:{"Nombre": "Hotel Carolina Del Mar 4 dias - 3 noches", "Tour": "Tour Privado Piedras de Donama en Sierra Nevada de Santa Marta", "precio": 999999}
    },
    4: {
        1:{"Nombre": "Hostel Casa de las Palmas 4 dias - 3 noches", "Tours": "Visita Puerto Nariño, Tres Fronteras y la Reserva Marasha ", "precio": 845000},
        2:{"Nombre": "Hotel Yurupary 3 dias - 2 noches", "Tours": "Visita la reserva Natural Kindiwaira y la cascada fin del Mundo en Putumayo", "precio": 850000 }
    }
}

import time ##Se importa time para hacer pequeñas pausas en la ejecución del codigo.

##Creando funciones
##Fución para validar que la entrada sea un numero entero
def validar_entrada(mensaje):
    entrada = input(mensaje).strip()##quitando los espacios en blanco
    if entrada.isdigit():##.isdigit verifica si la cadena es un numero
        return int(entrada)##Retornamos la entrada 
    else:
        print("Ingresa un valor numerico")
        return validar_entrada(mensaje)##En caso que la entra sea algo diferente a un numero volvemos a llamar la función    
##Fución que imprime en pantalla los destinos disponibles desde el diccionario vuelos
def destinos():
    print("\033c",end="")
    print("***Elige un destino***")
    for clave, valor in vuelos.items():
        print(f"{clave}. {valor['Ciudad']}.")
    opcion_destino = validar_entrada("Ingresa una opción: ")
    if opcion_destino > 0 and opcion_destino <= len(vuelos):
        return opcion_destino
    else:
        print("***Ingresa una opción valida***")
        time.sleep(1)
        return destinos()    

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
    ##Validando que el diccionario no es vacio
    if len(diccionario_usuarios) == 0:
        print("***No hay usuarios registrados***")
    else:
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
        
def numero_pasajeros():
    print("\033c", end="")## Limpiar consola
    usuarios_viaje = validar_entrada("Ingrese la cantidad de personas que viajan: ")
    contador = usuarios_viaje
    while True:
        crea_usuario()
        contador -= 1
        if contador == 0:
            break
    return usuarios_viaje

def crea_paquete_turistico():
    """"comentario sobre la funcion"""
    print("\033c", end="")## Limpiar consola
    usuarios_viaje = numero_pasajeros()      
    opcion = destinos()
    print("Reservar vuelo.")
    reservar_vuelo(opcion,usuarios_viaje)
    print("Reservar hotel.")
    reservar_hotel(opcion,usuarios_viaje)
    
def reservar_vuelo(clave,pasajeros):
    """comentario sobre la funcion"""
    print("\033c", end="")## Limpiar consola
    if clave in vuelos:
        destino_elegido = vuelos[clave]["Ciudad"]
        salidas = vuelos[clave]["salidas"]
        print(f"El valor de los vuelos para {destino_elegido} es:")
        for salida, valor in salidas.items():
            print(f"Salida {salida}: ${valor:,}")
        opcion_vuelo =input("Ingresa una opción(a,b,c): ").strip().lower()
        if opcion_vuelo.isdigit() or opcion_vuelo not in {'a','b','c'}:
            print("***Ingresa una opción valida***")
            time.sleep(1)
            print("\033c",end="")
            reservar_vuelo(clave,pasajeros)
        costo_total.append(salidas[opcion_vuelo])                                
    else:
        print("***Ingresa una opción valida***")
        time.sleep(1)
        return reservar_vuelo(clave, pasajeros)
    
def reservar_hotel(clave,huesped):
    """comentario sobre la funcion"""
    print("\033c", end="")## Limpiar consola
    if clave in hoteles:
        print("Seleccione una opción de hotel:")
        for clave_hotel in hoteles[clave]:
            hotel = hoteles[clave][clave_hotel]
            print(f"{clave_hotel}. {hotel['Nombre']}")
        opcion_hotel = validar_entrada("Ingresa una opción: ")
        if clave in hoteles and opcion_hotel in hoteles[clave]:
            
            hotel_elegido = hoteles[clave][opcion_hotel]
            print(f"Hotel: {hotel_elegido['Nombre']}")
            print(f"Tours: {hotel_elegido['Tours']}")
            valor_hotel = hotel_elegido['precio'] * huesped 
            costo_total.append(valor_hotel)
            print(f"Precio: ${costo_total}")
        else:
            print("***Ingresa una opción valida***")
            time.sleep(1)
            reservar_hotel(clave, huesped)  
def mostrar_compra():
    """comentario sobre la funcion"""

##Creando diccionario con las diferentes opciones
menu_opciones = {
    1:crea_usuario,
    2:eliminar_usuario,
    3:mostrar_usuarios,
    4:crea_paquete_turistico,
    5:mostrar_compra
}
##Creando diccionario vacio para almacenar a los usuarios
diccionario_usuarios ={}
##Creando lista de costos
costo_total = [] 
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
    print(" 5.Resumen de la compra")
    print(" 6.Salir")
    #Solicitando opcion al usuario
    opcion = validar_entrada("\n Ingresa una opcion: ")
    #Invocando Fución escogida por el usuario
    if opcion in menu_opciones:
        menu_opciones[opcion]()
    #Saliendo del menu      
    elif opcion == 6:
        print("***Gracias por usar nuestro servicio***")
        break
    #Mensaje en caso de que se ingrese un dato equivocado
    else:
        print("\n***Ingresa una opcion valida***\n")
