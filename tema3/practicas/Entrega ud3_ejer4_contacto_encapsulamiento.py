from enum import Enum

class Idioma(Enum):
    CASTELLANO = 'cs'
    VALENCIANO = 'va'
    INGLES = 'en'

class Contacto:
    idioma = Idioma.CASTELLANO

    @classmethod
    def validarCuentaCorreo(cls, cc):
        return cc.find('@') > 0

    @classmethod
    def validarTelefono(cls, telefono):
        if len(telefono) != 9:
            return False
        else:
            return True if telefono.isnumeric() else False

    @classmethod
    def cambiarIdioma(cls, idioma):
        if idioma in list(Idioma._value2member_map_):
            cls.idioma = idioma
        else:
            raise ValueError('El idioma no es correcto')

    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.correo =  correo
        self.telefono =  telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        if Contacto.validarTelefono(telefono):
            self.__telefono = telefono
        else:
            self.__telefono = ''
            raise ValueError('El teléfono no es correcto')
   
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo):
        if Contacto.validarCuentaCorreo(correo):
            self.__correo = correo
        else:
            self.__correo = ''
            raise ValueError('El correo no es correcto')
        
    def imprimir(self):
        if self.idioma == Idioma.CASTELLANO:
            print("Contacto:")
            print('  nombre -->', self.nombre)
            print('  teléfono -->', self.telefono)
            print('  cuenta de correo -->', self.cuenta_correo)
        elif self.idioma == Idioma.VALENCIANO:
            print("Contacte:")
            print('  nom -->', self.nombre)
            print('  telèfon -->', self.telefono)
            print('  compte correu -->', self.cuenta_correo)            
        else:
            print("Contact:")
            print('  name -->', self.nombre)
            print('  number phone -->', self.telefono)
            print('  e-mail -->', self.cuenta_correo)
    
    def __eq__(self, other):
        return (self.nombre == other.nombre and self.telefono == other.telefono and self.correo == other.correo)

if __name__ == "__main__":

    c1 = Contacto("Pepe", "757575757", "v@v.com")
    c1.imprimir()
    
    Contacto.cambiarIdioma('va')
    try:
        Contacto.cambiarIdioma('cs')
    except:
        print("Idioma incorrecto")

    # c2 = Contacto("Pepe", "66a", "v@v.com")

    c3 = Contacto("Pepe", "123456789", "v@c.com")

