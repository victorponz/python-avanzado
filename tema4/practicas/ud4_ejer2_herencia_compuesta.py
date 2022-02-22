from clases_base import Socio, Musico

class SocioMusico(Socio, Musico):
    def __init__(self, num_socio, nombre, cuota, dni, especialidad, descuento):
        super().__init__(num_socio, nombre, cuota)
        Musico.__init__(self, dni, nombre, especialidad)
        self.descuento = descuento

    def __str__(self):
        return super().__str__() + "\n" +  Musico.__str__(self) +  "\n" + "Tiene un descuento de " + str(self.descuento) + " € en actividades"


if __name__ == "__main__":
    sm = SocioMusico('1', 'Ana' , 10, "11111H", 'Violín', 5)
    print(sm, '\n')

    sm2 = SocioMusico('2', 'Pep' , 15, "22222H", 'Flauta', 6)
    print(sm2, '\n')

    