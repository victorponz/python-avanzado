class Personaje:
    @classmethod
    def validarEdad(cls, edad):
        return  isinstance(edad, int) and edad >= 0 and edad <= 150

    def __init__(self, nombre, edad, autor):
        self.nombre = nombre
        self.edad =  edad
        self.autor =  autor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if Personaje.validarEdad(edad):
            self.__edad = edad
        else:
            self.__telefono = ''
            raise ValueError('La edad debe ser menor de 150 años')
   
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor    

    def imprimir(self):
        print("Personaje:")
        print('  nombre -->', self.nombre)
        print('  edad -->', self.edad)
        print('  autor -->', self.autor)

    def __eq__(self, other):
        return (self.nombre == other.nombre and self.telefono == other.telefono and self.correo == other.correo)

    def __str__(self):
        return "{} tiene {} años y es de {}".format(self.nombre, self.edad, self.autor)
if __name__ == "__main__":

    p1 = Personaje("Mafalda", 100, "Quino")
    p1.imprimir()
    print(p1)
