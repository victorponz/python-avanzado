###################################
# UNIDAD 2 - Ejercicio 4          #
# Jugadores (ESQUEMA)             #
###################################
from doctest import ELLIPSIS
from socket import herror
import sqlite3

# DEFINICIÓN DE FUNCIONES --------------------------------------
def imprimir_registro(reg):
    print("Nombre: ", reg[0], "- Vida: ", reg[1], end=" ")    

def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    

    opc_correctas = ['1', '2', '3', '4', '5', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("========================================")            
        print("         GESTIONANDO JUGADORES          ")
        print("========================================")
        print(" 1 - Imprimir jugadores")
        print(" 2 - Modificar vida de jugador ")
        print(" 3 - Insertar nuevo jugador ")
        print(" 4 - Imprimir herramientas-jugador ")
        print(" 5 - Quitar herramienta-jugador ")
        print(" 0 - SALIR ")
        print("--------------------------")    
        opcion = input("Dame la opción: ")
        if opcion not in opc_correctas:
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion
    
def imprimir_jugadores(cursor):
    '''Imprimir jugadores existentes en la base de datos
       
       Parámetros de entrada: cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("IMPRIMIR JUGADORES")
    #Ejecutamos la consulta SQL
    cursor.execute("SELECT * FROM jugadores")
    #Recuperamos todos los registros con el método fetchall.
    registros = cursor.fetchall()
    for reg in registros:
        imprimir_registro(reg)
        print()
    pass


def existe_jugador(cursor, jugador):
    '''Comprueba si existe un jugador en la tabla JUGADORES.
       
       Parámetros de entrada: cursor de la bd y nombre del jugador
       Parámetros de salida: devuelve True si existe y False en otro caso
    '''
    sql = "SELECT * FROM JUGADORES WHERE NOMBRE = '" + jugador + "'"
   
    cursor.execute(sql)
    registro = cursor.fetchone()
    return (registro != None)
    
def lee_vida():
    '''Pide el valor "vida" por pantalla.
       
       Parámetros de entrada: no hay
       Parámetros de salida: número entero vida
    '''    
    correcto = False
    while not correcto:
        try:
            vida = int(input("Dame vida: "))
        except ValueError:
            print("Estábamos esperando un número entero. Por favor, vuelve a intentarlo.")
        else:
            correcto = True
    return vida
        
def modificar_vida(conexion, cursor):
    '''Modifica la vida de un jugador
       
       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("MODIFICAR VIDA")
    jugador = input("Dame jugador: ")
    vida = lee_vida()
    if existe_jugador(cursor, jugador):
        cursor.execute("UPDATE JUGADORES SET VIDA = ? WHERE NOMBRE = ?", (vida, jugador))
        print("La vida del jugador <{}> se ha modificado correctamente".format(jugador))    
    else:
        print("El jugador <%s> no existe" %(jugador))

def insertar_jugador(conexion, cursor):
    '''Inserta una nueva herramienta en la base de datos

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("INSERTAR JUGADOR")
    jugador = input("Dame jugador: ")
    vida = lee_vida()
    if not existe_jugador(cursor, jugador):
        cursor.execute("INSERT INTO JUGADORES VALUES(?, ?)", (jugador, vida))
        print("El jugador <{}> se ha insertado correctamente".format(jugador)) 
    else:
        print("El jugador ya existe")
    
        
        
def imprimir_herramientas_jugador(cursor):
    '''Imprimir las herramientas de un jugador
       
       Parámetros de entrada: cursor de la base de datos
       Parámetros de salida: no hay
    '''    
    print("HERRAMIENTAS JUGADOR")
    nombre = input('Dame el nombre del jugador: ')
    if existe_jugador(cursor, nombre):
        sql = """SELECT H.NOMBRE FROM LISTA_HERRAMIENTAS AS LH
                INNER JOIN JUGADORES AS J ON LH.JUGADOR = J.NOMBRE
                INNER JOIN HERRAMIENTAS AS H ON LH.HERRAMIENTA = H.NOMBRE WHERE J.NOMBRE = '"""
        sql += nombre + "'"
    
        cursor.execute(sql)
        registros = cursor.fetchall()
        if not registros:
            print("El jugador no tiene ninguna herramienta")
        else:
            print("Herramientas: ", end=" ")
            for reg in registros:
                print( reg[0], end=" - ") 
    else:
         print("No existe ningún jugador con dicho nombre")
        

def existe_herramienta_jugador(cursor, jugador, herramienta):
    '''Comprueba si existe el par jugador-herramienta.
       
       Parámetros de entrada: cursor de la bd, nombre del jugador y nombre de la herramienta
       Parámetros de salida: devuelve True si existe y False en otro caso
    '''
    sql = """SELECT H.NOMBRE FROM LISTA_HERRAMIENTAS AS LH
            INNER JOIN JUGADORES AS J ON LH.JUGADOR = J.NOMBRE
            INNER JOIN HERRAMIENTAS AS H ON LH.HERRAMIENTA = H.NOMBRE WHERE J.NOMBRE = '"""
    sql += jugador + "' AND H.NOMBRE = '" + herramienta + "'"
   
    cursor.execute(sql)
    registro = cursor.fetchone()
    return (registro != None)


def quitar_herramienta(conexion, cursor):
    '''Borrar herramienta de la base de datos
       
       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("QUITAR HERRAMIENTA")
    jugador = input("Dame jugador: ")
    herramienta = input("Dame herramienta: ")
    if existe_jugador(cursor, jugador):
        if existe_herramienta_jugador(cursor, jugador, herramienta):
            cursor.execute("DELETE FROM LISTA_HERRAMIENTAS WHERE JUGADOR = ? AND HERRAMIENTA = ?", (jugador, herramienta, ))
            print("Se ha eliminado la herramienta <{}> del jugador <{}> correctamente".format(herramienta, jugador))    
        else:
            print("El jugador <%s> no tiene la herramienta <%s>" %(jugador, herramienta))
    else:
        print("No existe ningún jugador con dicho nombre")

# PROGRAMA PRINCIPAL -------------------------------------------
conexion = sqlite3.connect("./voluntarios/ejers_voluntarios_ejer4.db")
cursor = conexion.cursor()

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1': #Imprimir jugadores
        imprimir_jugadores(cursor)
    elif opcion == '2': #Modificar vida de jugador
        modificar_vida(conexion, cursor)            
    elif opcion == '3': #Insertar nuevo jugador
        insertar_jugador(conexion, cursor)
    elif opcion == '4': #Imprimir herramientas-jugador
        imprimir_herramientas_jugador(cursor)
    elif opcion == '5': #Quitar herramienta-jugador
        quitar_herramienta(conexion, cursor)
    opcion = valida_opcion()
conexion.close()