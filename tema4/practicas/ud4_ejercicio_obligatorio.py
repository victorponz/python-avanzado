#############################################
# UNIDAD 4 - Ejercicio obligatorio          #
# Cocinando (ESQUEMA)                       #
#############################################
from clases_base import Articulo

# DEFINICIÓN DE CLASES --------------------------------------
class Ingrediente(Articulo):
    def __init__(self, codigo, modelo, cantidad):
        super().__init__(codigo, modelo)
        self.cantidad = cantidad

    def __str__(self):
        return ("({}, {}) --> {}".format(self.codigo, self.modelo, self.cantidad) )

class Receta():
    def __init__(self, ingredientes, elaboracion):
        self.ingredientes = ingredientes
        self.elaboracion = elaboracion

    def __str__(self):        
        cadena = '--> Ingredientes de la receta:\n'        
        if len(self.ingredientes) == 0:
            cadena += '\t(no seleccionados)\n'    
        else:
            for p in self.ingredientes:
                cadena += '\t' + str(p) + '\n'
            
        cadena += '---> Elaboración:\n'
    
        if not self.elaboracion is None:
            cadena += '\t' + (self.elaboracion) + "\n"
        else:
            cadena += '\t(no establecida)\n'
        return cadena    

    def anyadir_ingrediente(self, ingrediente):        
        self.ingredientes.append(ingrediente)

    
# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    

    opc_correctas = ['1', '2', '3', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("==========================")            
        print("        COCINANDO         ")
        print("==========================")
        print(" 1 - Añadir ingrediente ")
        print(" 2 - Escribir elaboración")
        print(" 3 - Mostrar receta")
        print(" 0 - SALIR ")
        print("--------------------------")    
        opcion = input("Dame la opción: ")
        if opcion not in opc_correctas:
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion

def elegir_ingrediente(receta):
    '''Crear un objeto Ingrediente y añadirlo a la lista.

       Parámetros de entrada: lista de objetos Ingrediente
       Parámetros de entrada: lista de objetos Ingrediente modificada
    '''
    print("AÑADIR INGREDIENTE: ")
    codigo = input('Dame el código: ')
    nombre = input('Dame el nombre: ')
    cantidad = input('Dame el cantidad: ')

    i1 = Ingrediente(codigo, nombre, cantidad)
    receta.anyadir_ingrediente(i1)
    print("Ingrediente:", i1)
    return receta
    
    
def escribir_elaboracion(receta):
    '''Rellenar el atributo "elaboracion".

       Parámetros de entrada: receta
       Parámetros de entrada: receta modificada
    '''
    print("ESCRIBIR ELABORACION: ")
    receta.elaboracion = input('Dame el elaboración: ')
    return receta

def mostrar_receta(receta):
    '''Imprime los datos de la receta

       Parámetros de entrada: receta
       Parámetros de entrada: nada
    '''
    print("RECETA: ")
    print(receta)


#PROGRAMA PRINCIPAL ---------------------------------------------
r = Receta([], None)    #Inicialmente está vacío

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1': #Crear objeto Ingrediente y añadir a la lista
        r = elegir_ingrediente(r)
    elif opcion == '2': #Rellenar elaboracion
        r = escribir_elaboracion(r)
    elif opcion == '3': #Mostrar receta
        mostrar_receta(r)
        
    opcion = valida_opcion()        