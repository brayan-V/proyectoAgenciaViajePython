"""Se desarrollan las funciones relacionadas con el usuario y su logica."""
import time ##Se importa time para hacer pequeñas pausas en la ejecución del codigo.

##Creando diccionario vacio para almacenar a los usuarios
diccionario_usuarios ={}
##Fución para validar que la entrada sea un numero entero
def validar_entrada(mensaje):
    entrada = input(mensaje).strip()##quitando los espacios en blanco
    if entrada.isdigit():##.isdigit verifica si la cadena es un numero
        return int(entrada)##Retornamos la entrada 
    else:
        print("Ingresa un valor numerico")
        return validar_entrada(mensaje)##En caso que la entra sea algo diferente a un numero volvemos a llamar la función
     
def crea_usuario():
    """Función que solicita los datos del usuario y 
    lo agrega al diccionario de usuarios"""
    print("\033c", end="") ##Limpiar consola
    id_usuario = validar_entrada("Ingresa la identificación del usuario: ")
    #Validando que no hayan identificiones duplicadas
    if id_usuario in diccionario_usuarios:
        print("***Identificación en uso, ingresa una nueva.***")
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
        identificacion = validar_entrada("Ingresa la identificación del clientes que deseas eliminar: ")
        ##Validando que la identificación exista en el diccionario    
        if identificacion in diccionario_usuarios:
            ##Eliminando al usuario con la funcion pop 
            diccionario_usuarios.pop(identificacion)
            print("***El usuario fue eliminado con exito***")
        else:
            print("***La identificación no existe***")
        
def mostrar_usuarios():
    """"Función que recorre nuestro diccionario de clientes e imprime en 
        pantalla sus datos."""
    print()
    ##Recorriendo el diccionario, usando la función .items() que nos retorna la clave y el valor
    if len(diccionario_usuarios) == 0:##Validando si el diccionario esta vacio
        print("***No hay usuarios registrados***")
    else:
        ##Imprimiendo a los usuarios
        print("Usuarios: ")
        for id, usuario in diccionario_usuarios.items():
            print(f"ID {id} {usuario['nombre']} {usuario['apellido']} {usuario['edad']} años")