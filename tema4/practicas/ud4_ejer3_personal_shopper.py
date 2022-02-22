###################################
# UNIDAD 4 - Ejercicio 3          #
# Personal shopper (ESQUEMA)      #
###################################
from ud4_ejer1_herencia_simple import Prenda,  Zapatos

#DEFINICIÓN DE CLASES ---------------------------------------------
#CLASE Conjunto
class Conjunto():
    def __init__(self, prendas, zapatos):
        self.prendas = prendas
        self.zapatos = zapatos

    def __str__(self):        
        cadena = '--> Prendas de ropa:\n'        
        if len(self.prendas) == 0:
            cadena += '\t(no seleccionadas)\n'    
        else:
            for p in self.prendas:
                cadena += '\t' + str(p) + '\n'
            
        cadena += '---> Zapatos:\n'
        if isinstance(self.zapatos, Zapatos):            
            cadena += '\t' + str(self.zapatos)
        else:
            cadena += '\t(no seleccionados)\n'
        
        return cadena    

    def anyadir_prenda(self, prenda):        
        self.prendas.append(prenda)

    def anyadir_zapatos(self, zapatos):
        self.zapatos = zapatos

# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    

    opc_correctas = ['1', '2', '3', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("================================")            
        print("       PERSONAL SHOPPER         ")
        print("================================")
        print(" 1 - Elegir prenda de ropa ")
        print(" 2 - Elegir zapatos")
        print(" 3 - Mostrar conjunto")
        print(" 0 - SALIR ")
        print("--------------------------")    
        opcion = input("Dame la opción: ")
        if opcion not in opc_correctas:
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion

def elegir_prenda(conjunto):
    '''Crear un objeto Prenda y añadirlo a la lista de prendas.

       Parámetros de entrada: lista de objetos Prenda
       Parámetros de entrada: lista de objetos Prenda modificada
    '''
    print("AÑADIR PRENDA: ")
    codigo = input('Dame el código: ')
    modelo = input('Dame el modelo: ')
    temporada = input('Dame la temporada: ')
    p1 = Prenda(codigo, modelo, temporada)
    conjunto.anyadir_prenda(p1)
    print("\Prenda: ", p1)
    return conjunto

def elegir_zapatos(conjunto):
    '''Crear un objeto Zapatos.

       Parámetros de entrada: objeto Conjunto
       Parámetros de entrada: objeto Conjunto modificado
    '''
    print("AÑADIR ZAPATOS: ")
    codigo = input("--> Dame el código: ")
    modelo = input("--> Dame el modelo: ")
    suela = input("--> Dame la suela: ")

    z = Zapatos(codigo, modelo, suela)
    print("\nZapatos: ", z)
    
    conjunto.zapatos = z    
    return conjunto

def mostrar_conjunto(conjunto):
    '''Imprime los datos de un conjunto de ropa

       Parámetros de entrada: objeto Conjunto
       Parámetros de entrada: nada
    '''
    print("CONJUNTO ELEGIDO: ")
    print(conjunto)

#PROGRAMA PRINCIPAL ---------------------------------------------
c = Conjunto([], None)    #Inicialmente está vacío

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1': #Crear objeto Prenda y añadir a la lista
        c = elegir_prenda(c)
    elif opcion == '2': #Crear objeto Zapatos
        c = elegir_zapatos(c)
    elif opcion == '3': #Mostrar conjunto
        mostrar_conjunto(c)
        
    opcion = valida_opcion()    