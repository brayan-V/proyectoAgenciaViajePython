"""Se desarrollan las funciones relacionadas con los vuelos y su logica"""
from usuarios import validar_entrada
import time
##Diccionario que almacela los destinos de los vuelos y su valor
vuelos = {
    1: {"Ciudad": "Bogota", "salidas": {"a": 130000, "b": 140000, "c": 150000}},
    2: {"Ciudad": "Medellin", "salidas": {"a": 145000, "b": 155000, "c": 165000}},
    3: {"Ciudad": "Santa Marta", "salidas": {"a": 160000, "b": 170000,  "c": 180000}},
    4: {"Ciudad": "Amazonas", "salidas": {"a": 175000, "b": 185000, "c": 200000}}
}
##Creando lista de costo vuelo
costo_vuelo = []
##Fución que imprime en pantalla los destinos disponibles desde el diccionario vuelos
def destinos():
    print("\033c", end="")
    print("***Elige un destino***")
    ##Recoremos el diccionario vuelos para extraer los destinos
    for clave, valor in vuelos.items():
        print(f"{clave}. {valor['Ciudad']}.")
    ##Se valida que la entrada sea un número entero
    opcion_destino = validar_entrada("Ingresa una opción: ")
    ##Se valida que la opción este en el rango disponible
    if 0 < opcion_destino <= len(vuelos):
        ##Almacenamos el nombre del destino en una variable
        destino = "Destino " + vuelos[opcion_destino]['Ciudad']
        ##Retornamos la opcion elegida con el destino
        return opcion_destino, destino
    else:
        print("***Ingresa una opción válida***")
        time.sleep(1)
        return destinos()
    
def reservar_vuelo(clave,pasajeros):
    """Función que nos permite seleccionar los vuelos para los diferentes destinos"""
    print("\033c", end="")## Limpiar consola
    ##Validamos si la clave se encuentra en el diccionario de vuelos
    if clave in vuelos:
        ##Extraemos el nombre del destino con la clave ingresada
        destino_elegido = vuelos[clave]["Ciudad"]
        ##Extramos el diccionario de salidas con la clave ingresada
        salidas = vuelos[clave]["salidas"]
        print(f"El valor de los vuelos para {destino_elegido} es:")
        for salida, valor in salidas.items():
            print(f"Salida {salida}: ${valor:,}")
        ##Pedimos la opción de vuelo y quitamos los espacios en blanco con .strip()
        ##y convertimos la opción en minuscula con .lower()
        opcion_vuelo =input("Ingresa una opción(a,b,c): ").strip().lower()
        ##Validamos si la opción es un número o con se encuentra entre las opciones
        if opcion_vuelo.isdigit() or opcion_vuelo not in {'a','b','c'}:
            print("***Ingresa una opción valida***")
            time.sleep(1)
            print("\033c",end="")
            reservar_vuelo(clave,pasajeros)
        else:
            ##Extraemos el valor del vuelo y lo almacenamos
            vuelo_total = salidas[opcion_vuelo] * pasajeros
            costo_vuelo.append(vuelo_total)
            print(f"Valor del vuelo para {pasajeros} es: {vuelo_total:,}")
            time.sleep(2)                              
    else:
        print("***Ingresa una opción valida***")
        time.sleep(1)
        ##Sino se ingresa una opcón valida, llamamos nuevamente a la función
        return reservar_vuelo(clave, pasajeros)
    
