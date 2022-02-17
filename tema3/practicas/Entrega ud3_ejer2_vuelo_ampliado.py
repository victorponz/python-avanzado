class Vuelo:
    def __init__(self, origen, destino, dia, clase = 'turista'):
        self.origen = origen
        self.destino = destino
        self.dia = dia
        self.clase = clase
    
    def imprimir(self):
        datos = "Datos del vuelo:\n"
        datos += "Origen -->" + self.origen + "\n"
        datos += "Destino -->" + self.destino + "\n"
        datos += "Día -->" + self.dia + "\n"
        datos += "Clase -->" + self.clase + "\n"
        print(datos)
    
    def __str__(self):
        return  "Origen: {} - Destino: {} - Día: {} - Clase: {}".format(self.origen, self.destino, self.dia, self.clase)

    def __eq__(self, other):
        return (self.origen == other.origen and self.destino == other.destino and self.dia == other.dia and self.clase == other.clase)

if __name__ == "__main__":
    v1 = Vuelo('Menorca', 'Valencia', '15-08', 'Primera')
    v1.imprimir()
    print(v1)
    
    v2 = Vuelo('Valencia', 'París', '15-08', '09-04')
    v2.imprimir()
    print(v2)
    
    v3 = Vuelo('Valencia', 'París', '15-08', '09-04')
    
    print(v1 == v2)

    print(v2 == v3)
