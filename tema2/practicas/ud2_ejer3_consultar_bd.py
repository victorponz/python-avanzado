######################################
# UNIDAD 2 - Ejercicio 3             #
# Consultar base de datos (ESQUEMA)  #
######################################
import re
import sqlite3

# DEFINICIÓN DE FUNCIONES --------------------------------------
def imprimir_registro(reg):
    print("Nombre: ", reg[0], "- Vida: ", reg[1], end=" ")    
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    

    opc_correctas = ['1', '2', '3', '4', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("========================================")            
        print("         CONSULTAR BASE DE DATOS        ")
        print("========================================")
        print(" 1 - Imprimir jugadores")
        print(" 2 - Imprimir herramientas-jugador ")
        print(" 3 - Consultar jugador")
        print(" 4 - Consultar herramienta-jugador")
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

def imprimir_herramientas_jugador(cursor):
    '''Imprimir las herramientas de un jugador
       
       Parámetros de entrada: cursor de la base de datos
       Parámetros de salida: no hay
    '''    
    print("HERRAMIENTAS JUGADOR")
    nombre = input('Dame el nombre del jugador: ')
    sql = """SELECT H.NOMBRE FROM LISTA_HERRAMIENTAS AS LH
            INNER JOIN JUGADORES AS J ON LH.JUGADOR = J.NOMBRE
            INNER JOIN HERRAMIENTAS AS H ON LH.HERRAMIENTA = H.NOMBRE WHERE J.NOMBRE = '"""
    sql += nombre + "'"
   
    cursor.execute(sql)
    registros = cursor.fetchall()
    if not registros:
        print("No existe ningún jugador con dicho nombre")
    else:
        print("Herramientas: ", end=" ")
        for reg in registros:
            print( reg[0], end=" - ")  

def consultar_jugador(cursor):
    '''Comprueba si existe un jugador en la tabla JUGADORES.
       
       Parámetros de entrada: cursor de la bd 
       Parámetros de salida: no hay
    '''
    print("CONSULTAR JUGADOR")
    nombre = input('Dame el nombre del jugador: ')
    sql = "SELECT * FROM JUGADORES WHERE NOMBRE = '" + nombre + "'"
   
    cursor.execute(sql)
    registro = cursor.fetchone()
    if registro == None:
        print("No existe ningún jugador con dicho nombre")
    else:
        imprimir_registro(registro)
        

def consultar_herramienta_jugador(cursor):
    '''Comprueba si existe el par jugador-herramienta.
       
       Parámetros de entrada: cursor de la bd
       Parámetros de salida: no hay
    '''
    print("CONSULTAR HERRAMIENTA-JUGADOR")
    nombre = input('Dame el nombre del jugador: ')
    herramienta = input('Dame herramienta: ')
    sql = """SELECT H.NOMBRE FROM LISTA_HERRAMIENTAS AS LH
            INNER JOIN JUGADORES AS J ON LH.JUGADOR = J.NOMBRE
            INNER JOIN HERRAMIENTAS AS H ON LH.HERRAMIENTA = H.NOMBRE WHERE J.NOMBRE = '"""
    sql += nombre + "' AND H.NOMBRE = '" + herramienta + "'"
   
    cursor.execute(sql)
    registro = cursor.fetchone()
    if registro == None:
        print("El jugador <%s> no tiene la herramienta <%s>" %(nombre, herramienta))
    else:
        print("El jugador <%s> sí tiene la herramienta <%s>" %(nombre, herramienta))
    pass


# PROGRAMA PRINCIPAL -------------------------------------------
conexion = sqlite3.connect("./voluntarios/ejers_voluntarios_ejer3.db")
cursor = conexion.cursor()

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1': #Imprimir jugadores
        imprimir_jugadores(cursor)
    elif opcion == '2': #Imprimir herramientas-jugadores
        imprimir_herramientas_jugador(cursor)
    elif opcion == '3': #Consultar jugador
        consultar_jugador(cursor)
    elif opcion == '4': #Consultar herramienta-jugador
        consultar_herramienta_jugador(cursor)
        
    opcion = valida_opcion()
conexion.close()