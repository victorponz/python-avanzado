############################################
# UNIDAD 1 - Ejercicio obligatorio         #
# Lista de vuelos (ESQUEMA)                #
############################################

vuelos = [{'origen':'Valencia', 'destino':'Menorca', 'día':'15-08', 'clase':'turista'},
          {'origen':'Valencia', 'destino':'Tenerife', 'día':'20-08', 'clase':'turista'},
          {'origen':'París', 'destino':'Valencia', 'día':'15-08', 'clase':'primera'},
          {'origen':'Atenas', 'destino':'Valencia', 'día':'20-08', 'clase':'primera'} ]

# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    
    
    #Mostramos el menú y solicitamos la operación al usuario
    opciones_validas = ['1', '2', '3', '4', '5', '0']
    opcion = ''
    while (opcion not in opciones_validas):
        print()
        print("=========================")            
        print("     LISTA DE VUELOS     ")
        print("=========================")
        print(" 1 - Imprimir datos vuelos")
        print(" 2 - Buscar por origen ")
        print(" 3 - Imprimir un vuelo")        
        print(" 4 - Cambiar fecha de vuelo ")        
        print(" 0 - SALIR ")
        print("-----------------------------")    
        opcion = input("Dame la opción: ")
        if (opcion not in opciones_validas):
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion


def imprimir(lista):
    '''Función que imprime la lista de vuelos.
    
       Parámetros de entrada: lista de diccionarios
       Parámetros de salida: no hay
    '''
    print("IMPRIMIR VUELOS:")
    for vuelo in lista:
        for k, v in vuelo.items():
            print(k,  " - ",  v, end=', ')
        print()
    print()

def buscar_origen(lista):
    '''Función que busca un vuelo dentro de una lista de vuelos.
    
       Parámetros de entrada: lista de diccionarios
       Parámetros de salida: no hay
    '''
    print("BUSCAR ORIGEN:")
    origen = input("Introduce ciudad de origen: ")
    encontrado = False
    for vuelo in lista:
        if (vuelo['origen']  == origen):
            encontrado = True
            for k, v in vuelo.items():
                print(k,  " - ",  v, end=', ')
            print()
    if (not encontrado):
        print("No se ha encontrado ningún vuelo con origen '%s'" % origen)
    print()

def buscarVuelo(lista, origen, destino):
    for vuelo in lista:
        if (vuelo['origen']  == origen) and (vuelo['destino'] == destino):
            return vuelo
    return None


def imprimir_vuelo(lista):
    '''Función que imprime los datos de un vuelo.
    
       Parámetros de entrada: lista de diccionarios
       Parámetros de salida: no hay
    '''
    print("IMPRIMIR VUELO:")
    origen = input("Introduce ciudad de origen: ")
    destino = input("Introduce ciudad de destino: ")
    vuelo = buscarVuelo(lista, origen, destino)
    if vuelo:
        for k, v in vuelo.items():
            print(k,  " - ",  v, end=', ')
        print()
    else:
        print("No se ha encontrado ningún vuelo con origen '%s' y destino '%s'" % (origen, destino))
    print()


def cambiar_fecha(lista):
    '''Función que cambia la fecha de un vuelo.
    
       Parámetros de entrada: lista de diccionarios
       Parámetros de salida: lista de diccionarios actualizada
    '''
    print("CAMBIAR FECHA DE VUELO:")
    origen = input("Introduce ciudad de origen: ")
    destino = input("Introduce ciudad de destino: ")
    vuelo = buscarVuelo(lista, origen, destino)
    if vuelo:
        vuelo['día'] = input('Introduce la fecha del vuelo: ')
    
    return lista
        
        
        

# PROGRAMA PRINCIPAL -------------------------------------------
opcion = valida_opcion()
while opcion != '0':          
    #Respondemos a la opción seleccionada    
    if opcion == '1':  
        imprimir(vuelos)
    elif opcion == '2': 
        buscar_origen(vuelos)
    elif opcion == '3': 
        imprimir_vuelo(vuelos)
    elif opcion == '4': 
        vuelos = cambiar_fecha(vuelos)
    opcion = valida_opcion()
    
print("Hasta pronto")
