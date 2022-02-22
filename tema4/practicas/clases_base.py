###################################
# CLASES BASE PARA LOS EJERCICIOS #
###################################

#Aunque lo adecuado sería trabajar con atributos ocultos,
#vamos a obviarlo para simplificar las clases.

#CLASE Articulo
class Articulo:
    #métodos redefinidos
    def __init__(self, codigo, modelo):
        self.codigo = codigo 
        self.modelo = modelo

    def __str__(self):
        return "<" + self.codigo + "> es <" + self.modelo + ">"
    
#CLASE Socio
class Socio:
    #métodos redefinidos
    def __init__(self, num_socio, nombre, cuota):
        self.num_socio = num_socio
        self.nombre = nombre
        self.cuota = cuota
        
    def __str__(self):
        return self.nombre + " (socio nº " + self.num_socio + ") paga " + str(self.cuota) + "€ de cuota."


#CLASE Musico
class Musico:
    #métodos redefinidos
    def __init__(self, dni, nombre, especialidad):
        self.dni = dni
        self.nombre = nombre
        self.especialidad = especialidad
        
    def __str__(self):
        return self.nombre + " (dni: " + self.dni + ") practica " + self.especialidad + "."    
