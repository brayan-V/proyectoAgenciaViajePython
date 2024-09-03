"""Importamos las funciones nesesarias para la ejecución del programa"""
from usuarios import validar_entrada, crea_usuario, eliminar_usuario, mostrar_usuarios, diccionario_usuarios
from vuelos import destinos, reservar_vuelo, costo_vuelo
from hoteles import reservar_hotel, costo_hotel
import sys, time
##Creando lista donde se almacena el destino, hotel y tour elegido
destino_hotel_tour = []
##Función que pregunta el número de pasajeros y realiza su creacion usando otra función
def numero_pasajeros():
    print("\033c", end="")##Limpiar consola
    usuarios_viaje = validar_entrada("Ingrese la cantidad de personas que viajan: ")##Validando entrada
    contador = usuarios_viaje
    ##Bucle para ir creando a los usuarios
    while contador > 0:
        crea_usuario()
        time.sleep(0.5)
        contador -= 1
        if contador == 0:
            break
    return usuarios_viaje ##Retornamos el número de usuarios
##Función para crear el paquete turistico haciendo llamado a las diferentes funciónes
def crea_paquete_turistico():
    ##Capturamos el número de usuarios desde la función numero_pasajeros
    usuarios_viaje = numero_pasajeros()
    ##Capturamos la clave y el destino que nos retorna la función destinos
    clave_destino, destino = destinos()
    ##Invocamos las funciones con la clave elegida y el número de usuarios
    reservar_vuelo(clave_destino, usuarios_viaje)
    hotel, tour = reservar_hotel(clave_destino, usuarios_viaje)
    ##Almacenamos el destino, hotel y tour elegido
    destino_hotel_tour.append(destino)
    destino_hotel_tour.append(hotel)
    destino_hotel_tour.append(tour)
##Función que nos muestra un resumen de la compra
def mostrar_compra():
    print("\033c", end="")##Limpiar consola
    ##Validamos que los diccionaro y listas no esten vacios
    if  (diccionario_usuarios != {}) and (costo_hotel and costo_vuelo) != []:
        ##Se suman los valores contenidos en las listas
        hotel = sum(costo_hotel)
        vuelo = sum(costo_vuelo)
        ##Se calcula el costo total del viaje
        costo_total = hotel + vuelo
        ##Se realiza la impresión del resumen de la compra
        print("RESUMEN DE LA COMPRA:" + "\n")
        ##Mostramos el número de usuarios
        print(f"Total usuarios: {len(diccionario_usuarios)}")
        ##Mostramos los usuarios registrados llamando la función mostrar_usuarios
        mostrar_usuarios()
        print()
        ##Imprimimos los datos almacenados en la lista
        for datos in destino_hotel_tour:
            print(f"-{datos}")
        ##Imprimiendo costos del paquete
        print(f"\n-->Costo total del vuelo: ${vuelo:,}")
        print(f"-->Costo total del hotel: ${hotel:,}")
        print(f"-->Precio total del viaje: ${costo_total:,}")
        time.sleep(1)
        print("\n"+"***Gracias por usar nuestro servicio***")
        sys.exit(0)
    else:
        print("\033c", end="")##Limpiar consola
        print("***No hay compras registradas***")

##Función que con tiene el diccionario de funciones e imprime el menú de opciones
def main():
    ##Diccionario que almacena la funciones que seran usadas en el menú
    menu_opciones = {
        1: crea_paquete_turistico,
        2: mostrar_usuarios,
        3: eliminar_usuario,
        4: mostrar_compra
    }
    ##Creando bucle para repetir el menú
    while True:
        mensaje_bienvenida ="\nBienvenido al menú de la Agencia"
        print(mensaje_bienvenida)
        print("*" * len(mensaje_bienvenida))
        #Mostrando opciones del menú en consola       
        print("\n1.Crear el paquete turístico\n2.Mostrar usuarios\n3.Eliminar usuario \n4.Resumen de la compra\n5.Salir")
        #Solicitando opción al usuario
        opcion = validar_entrada("\nIngresa una opción: ")##Validando entrada
        #Invocando Función escogida por el usuario
        if opcion in menu_opciones:
            menu_opciones[opcion]()
            #Saliendo del menu 
        elif opcion == 5:
            print("***Gracias por usar nuestro servicio***")
            break
        else:
            print("***Ingresa una opción válida***")
##Invocamos nuestra función principal
main()