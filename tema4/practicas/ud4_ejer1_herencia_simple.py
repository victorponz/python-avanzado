from clases_base import Articulo

class Prenda(Articulo):
    def __init__(self, codigo, modelo, temporada):
        super().__init__(codigo, modelo)
        self.temporada = temporada

    def __str__(self):
        return super().__str__() + " temporada <" + self.temporada + ">"

class Zapatos(Articulo):
    def __init__(self, codigo, modelo, suela):
        super().__init__(codigo, modelo)
        self.suela = suela

    def __str__(self):
        return super().__str__() + " suela <" + self.suela + ">"


if __name__ == "__main__":
    p1 = Prenda("P1", "Pantalón corto", "Verano")
    print(p1)
    p2 = Prenda("P2", "Blusa ligera", "Primavera")
    print(p2)
    p3 = Prenda("P3", "Falda larga", "Invierno")
    print(p3)

    z1 = Zapatos("Z1", "Salón", "Tacón 7 cm")
    print(z1)
    z2 = Zapatos("Z2", "Sandalias", "Cuero bajo")
    print(z2)
    
    