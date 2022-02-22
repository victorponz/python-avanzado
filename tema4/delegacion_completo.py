#Importamos la clase "Persona"
from persona import Persona

#Creamos la clase "Asociacion"
class Asociacion:
    #métodos redefinidos
    def __init__(self, cif, nombre, fecha, representante, afiliados):
        self.CIF = cif
        self.nombre = nombre
        self.fecha_creacion = fecha
        self.representante = representante
        self.afiliados = afiliados
        
    def __str__(self):
        return 'La "' + self.nombre + '" se creó en ' + self.fecha_creacion + \
               ' y su representante es ' + self.representante.__str__() + '.'
    
    def compara_representantes(self, asociacion):
        if (self.representante == asociacion.representante):
            respuesta = "SI"
        else:
            respuesta = "NO"
        print("La asociación <" + self.CIF + "> y la asociación <" + asociacion.CIF + "> " + \
              respuesta + " comparten el mismo representante.")
    
    def alta_afiliado(self, dni, nombre):
        nuevo = Persona(dni, nombre)
        self.afiliados.append(nuevo)
    
    def baja_afiliado(self, dni):
        lista = self.afiliados
        for i in range(len(lista)):
            if (lista[i].dni == dni):
                lista.pop(i)
                print('Afiliado {0} dado de baja de la asociación "{1}" correctamente.'.format(dni, self.nombre))
                break
    
    def imprime_afiliados(self):
        print("AFILIADOS de {0}: ".format(self.CIF))
        for a in self.afiliados:
            print(a)
        print()
    
    
#Programa principal --------------------------------------------------------------
print("-- ASOCIACIONES EXISTENTES --")
r1 = Persona("11111111H", "Armando")
a1 = Asociacion("1", "Asociación de vecinos", "01-01-2014", r1, [])
print(a1)

r2 = Persona("22222222J", "Pepita")
a2 = Asociacion("2", "Programando juntos", "01-01-2016", r2, [])
print(a2)

a3 = Asociacion("3", "Club de cocina", "01-01-2020", r2, [])
print(a3)

print("\n-- COMPARANDO REPRESENTANTES --")
a1.compara_representantes(a2)
a1.compara_representantes(a3)
a2.compara_representantes(a3)

print("\n-- ALTA DE AFILIADOS --")
a1.alta_afiliado("11111111H", "Armando");
a1.alta_afiliado("33333333P", "Ana")
a1.alta_afiliado("44444444A", "Charles")
a1.alta_afiliado("55555555K", "Mary")
a1.imprime_afiliados()

a2.alta_afiliado("44444444A", "Charles")
a2.alta_afiliado("66666666Q", "Joan")
a2.alta_afiliado("77777777B", "Mireia")
a2.imprime_afiliados()

a3.imprime_afiliados()

print("\n-- BAJA DE AFILIADOS --")
a1.baja_afiliado("55555555K")
a2.baja_afiliado("66666666Q")

print("\n-- AFILIADOS ACTUALES --")
a1.imprime_afiliados()
a2.imprime_afiliados()