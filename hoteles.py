"""Se desarrollan las funciones relacionadas con los hoteles y su logica"""
from usuarios import validar_entrada
import time
##Diccionario que almacena los hoteles, tours y precios
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
        3:{"Nombre": "Hotel Carolina Del Mar 4 dias - 3 noches", "Tours": "Tour Privado Piedras de Donama en Sierra Nevada de Santa Marta", "precio": 999999}
    },
    4: {
        1:{"Nombre": "Hostel Casa de las Palmas 4 dias - 3 noches", "Tours": "Visita Puerto Nariño, Tres Fronteras y la Reserva Marasha ", "precio": 845000},
        2:{"Nombre": "Hotel Yurupary 3 dias - 2 noches", "Tours": "Visita la reserva Natural Kindiwaira y la cascada fin del Mundo en Putumayo", "precio": 850000 }
    }
}
##Creando lista de costo hotel
costo_hotel = []
def reservar_hotel(clave,huesped):
    """Fumción que nos permite seleccionar el hotel para los diferentes destinos"""
    print("\033c", end="")## Limpiar consola
    ##Validamos si la clave se encuntra en el diccionario hoteles
    if clave in hoteles:
        print("Seleccione una opción de hotel:")
        for clave_hotel in hoteles[clave]:##Recorriendo el diccionario hoteles
            ##Extraemos el hotel con la clave ingresada
            hotel = hoteles[clave][clave_hotel]
            ##Imprimiedo el nombre de los hoteles con su respectivo tour y precio
            print(f"{clave_hotel}. {hotel['Nombre']} {hotel['precio']:,}"+"\n   "+(f"Tour: {hotel['Tours']}"))
        opcion_hotel = validar_entrada("Ingresa una opción: ")##Validamos la entrada
        ##Validamos si la clave ingresada y la opción elegida se encuentra en hoteles
        if clave in hoteles and opcion_hotel in hoteles[clave]:
            ##Almacenamos el hotel elegido en una variable            
            hotel_elegido = hoteles[clave][opcion_hotel]
            ##Extraemos el valor del hotel y lo almacenamos 
            valor_hotel = hotel_elegido['precio'] * huesped 
            costo_hotel.append(valor_hotel)
            print("\033c", end="")## Limpiar consola
            print(f"Precio del hotel más tour es: ${valor_hotel:,}")
            ##Retornando nombre del hotel y tour elegido
            return hotel_elegido['Nombre'], hotel_elegido['Tours']
        else:
            print("***Ingresa una opción valida***")
            time.sleep(1)
            ##Sino se ingresa una opcón valida, llamamos nuevamente a la función
            reservar_hotel(clave, huesped)