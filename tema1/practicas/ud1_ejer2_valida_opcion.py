# This Python file uses the following encoding: utf-8

def valida_opcion():
    """Comprueba que la opción elegida en el menú es la correcta de entre los valores 0 a 5."""
    incorrecto = True
    while(incorrecto):
        print("=============================")
        print("   GAMIFICACIÓN EN EL AULA")
        print("=============================")
        print(" 1 - Cargar datos del fichero")
        print(" 2 - Imprimir datos")
        print(" 3 - Jugar")
        print(" 4 - Guardar")
        print(" 5 - Cambiar contraseña")
        print(" 0 - SALIR")
        print("-----------------------------")

        num = int(input('Dame la opción: '))
        incorrecto = not (num >=0 and num <=5)
        if (incorrecto):
            print("Por favor, vuelve a intentarlo")
        else:            
            return num
            
opcion = valida_opcion()
print("La opción seleccionada es: %d" % opcion)