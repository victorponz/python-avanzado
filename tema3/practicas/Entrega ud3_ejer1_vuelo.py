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

if __name__ == "__main__":
    v1 = Vuelo('Menorca', 'Valencia', '15-08', 'Primera')
    v1.imprimir()
    
    v2 = Vuelo('Valencia', 'París', '15-08', '09-04')
    v2.imprimir()
    