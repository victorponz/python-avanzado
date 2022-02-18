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
    def cambiarIdioma(cls, idioma):
        if idioma in list(Idioma._value2member_map_):
            cls.idioma = idioma
        else:
            raise ValueError('El idioma no es correcto')

    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        if Contacto.validarCuentaCorreo(correo):
            self.correo = correo
        else:
            raise ValueError('El correo no es correcto')

    
    def imprimir(self):
        datos = "Datos del contacto:\n"
        datos += "Nombre -->" + self.nombre + "\n"
        datos += "Teléfono -->" + self.telefono + "\n"
        datos += "Correo -->" + self.correo + "\n"
        print(datos)
    
    def __str__(self):
        return  "Origen: {} - Destino: {} - Día: {} - Clase: {}".format(self.origen, self.destino, self.dia, self.clase)

    def __eq__(self, other):
        return (self.nombre == other.nombre and self.telefono == other.telefono and self.correo == other.correo)

if __name__ == "__main__":

    c1 = Contacto("Pepe", "75757575", "v@v.com")

    Contacto.cambiarIdioma('va')
    try:
        Contacto.cambiarIdioma('cs')
    except:
        print("Idioma incorrecto")
