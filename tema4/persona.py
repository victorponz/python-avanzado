class Persona:
    #atributos de clase
    idioma = "cs"
    
    #métodos de objeto
    def __init__(self, dni, nombre): #constructor
        self.dni = dni
        self.nombre = nombre
    
    def __str__(self):
        return ("(" + self.dni + ", " + self.nombre + ")")
    
    def __eq__(self, otro):
        return ((self.dni == otro.dni) and (self.nombre == otro.nombre))
        
    #manejo atributos ocultos
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if (self.dni_es_correcto(dni) == 0):
            self.__dni = dni
        else:
            self.__dni = ""
            raise ValueError("Formato incorrecto del DNI")
            
    def imprimir(self):
        if Persona.idioma == "cs":
            return "Dni: " + self.dni + ", Nombre: " + self.nombre
        elif self.idioma == "va":
            return "Dni: " + self.dni + ", Nom: " + self.nombre
        else:
            return "ID Card: " + self.dni + ", Name: " + self.nombre

    @classmethod
    def cambiarIdioma(cls, idioma):
        cls.idioma = idioma

    @staticmethod
    def dni_es_correcto(dni):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni)!=9:
            return -1
        else:
            letra = dni[8]
            num = int(dni[:8])
            if letra.upper() != letras[num % 23]:
                return -1
            else:
                return 0

