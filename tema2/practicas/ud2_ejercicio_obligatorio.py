########################################
# UNIDAD 2 - Ejercicio obligatorio     #
# Credenciales de jugadores (ESQUEMA)  #
########################################
from curses.ascii import controlnames
import sqlite3
from sre_constants import JUMP

def imprimir_registro(reg):
    print("Nombre: ", reg[0], "- Vida: ", reg[1], end=" ")    

# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    

    opc_correctas = ['1', '2', '3', '4', '5', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("==================================")            
        print("     CREDENCIALES JUGADORES       ")
        print("==================================")
        print(" 1 - Imprimir jugadores")
        print(" 2 - Validar credencial ")       
        print(" 3 - Cambiar credencial ")
        print(" 4 - Insertar nuevo jugador ")
        print(" 5 - Borrar jugador ")
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
    cursor.execute("SELECT * FROM jugadores AS J INNER JOIN CREDENCIALES AS C ON J.NOMBRE = C.USUARIO")
    #Recuperamos todos los registros con el método fetchall.
    registros = cursor.fetchall()
    for reg in registros:
        imprimir_registro(reg)
        print()

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
    
def existe_credencial(cursor, usuario, contras):
    '''Comprueba si existe una credencial en la tabla CREDENCIALES.
       
       Parámetros de entrada: cursor de la bd, usuario y contraseña.
       Parámetros de salida: devuelve True si existe y False en otro caso
    '''
    cursor.execute("SELECT * FROM CREDENCIALES WHERE USUARIO = ? AND CONTRASENYA = ?", (usuario, contras))
    registro = cursor.fetchone()
    return registro != None

def validar_credencial(cursor):
    '''Comprueba si existe el par jugador-contrasenya.
       
       Parámetros de entrada: cursor de la bd
       Parámetros de salida: no hay
    '''
    print("VALIDAR CREDENCIAL")
    jugador = input("Dame jugador: ")
    contras = input("Dame contraseña: ")
    
    if (existe_credencial(cursor, jugador, contras)):
         print("[{}/{}] sí es una credencial válida".format(jugador, contras))    
    else:
         print("[{}/{}] no es una credencial válida".format(jugador, contras))  
    
def cambiar_credencial(conexion, cursor):
    '''Modifica la contraseña de un jugador
       
       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("CAMBIAR CREDENCIAL")
    jugador = input("Dame jugador: ")
    if (not existe_jugador(cursor, jugador)):
        print("ERROR: el usuario [{}] no existe".format(jugador))    
    else:
        contras = input("Dame contraseña vieja: ")
        if (not existe_credencial(cursor, jugador, contras)):
            print("[{}/{}] no es una credencial válida".format(jugador, contras))  
        else:
            contrasNueva = input("Dame contraseña nueva: ")
            cursor.execute("UPDATE CREDENCIALES SET CONTRASENYA = ? WHERE USUARIO = ?", (contrasNueva, jugador))
            conexion.commit();     
        
def insertar_jugador(conexion, cursor):
    '''Inserta una nueva herramienta en la base de datos

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("INSERTAR JUGADOR")
    jugador = input("Dame jugador: ")
    contras = input("Dame contraseña: ")
    vida = lee_vida()

    if (existe_jugador(cursor, jugador)):
        print("ERROR: el usuario [{}] ya existe".format(jugador))    
    else:
        cursor.execute("INSERT INTO JUGADORES VALUES(?, ?)", (jugador, vida))
        cursor.execute("INSERT INTO CREDENCIALES VALUES(?, ?)", (jugador, contras))
        conexion.commit()
        
def borrar_jugador(conexion, cursor):
    '''Borra el jugador y sus credenciales de la base de datos
       
       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("BORRAR JUGADOR")
    jugador = input("Dame jugador: ")
  
    if (not existe_jugador(cursor, jugador)):
        print("ERROR: el usuario [{}] no existe".format(jugador))    
    else:
        cursor.execute("DELETE FROM CREDENCIALES WHERE USUARIO = ?", (jugador,))
        cursor.execute("DELETE FROM JUGADORES WHERE NOMBRE = ?", (jugador,))      
        conexion.commit()

# PROGRAMA PRINCIPAL -------------------------------------------
conexion = sqlite3.connect('bd/ejer_obligatorio.db') #Creamos la conexión a la base de datos
cursor = conexion.cursor() #Creamos el cursor

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1': #Imprimir jugadores
        imprimir_jugadores(cursor)
    elif opcion == '2': #Validar credencial
        validar_credencial(cursor)            
    elif opcion == '3': #Cambiar credencial
        cambiar_credencial(conexion, cursor)
    elif opcion == '4': #Insertar nuevo jugador
        insertar_jugador(conexion, cursor)    
    elif opcion == '5': #Borrar jugador
        borrar_jugador(conexion, cursor)
    opcion = valida_opcion()
conexion.close()