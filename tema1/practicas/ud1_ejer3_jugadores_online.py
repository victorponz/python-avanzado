# This Python file uses the following encoding: utf-8

from calendar import c


def valida_opcion():
    """Comprueba que la opción elegida en el menú es la correcta de entre los valores 1 a 3."""
    incorrecto = True
    while(incorrecto):
        print("=============================")
        print("      JUGADORES ON LINE")
        print("=============================")
        print(" 1 - Llega un jugador nuevo")
        print(" 2 - Se va un jugador")
        print(" 3 - FIN")
        print("-----------------------------")

        num = int(input('Dame la opción: '))
        incorrecto = not (num >=0 and num <=3)
        if (incorrecto):
            print("Por favor, elige una opción entre 1 y 3")
        else:            
            return num

def imprimeJugadores(jugadores):
    for i in range(len(jugadores)):
        print(jugadores[i], "-", end=" ")
    print()

def juegoOnLine():
    jugadores = ["mario", "mafalda", "luigi", "esther", "heidi", "songoku", "beauty", "beast"]
    
    continuar = True
    while (continuar):
        imprimeJugadores(jugadores)
        opcion = valida_opcion()
        print (opcion)
        if opcion == 1:
            jugador = input('¿Quién eres? ')
            print()
            print("Bienvenid@ jugador", jugador)
            print()
            jugadores.append(jugador)
        elif opcion == 2:
            if (len(jugadores) > 0):
                print("Adiós al jugador: " + jugadores.pop(0))
                print()
        else:
            continuar = False

        

juegoOnLine()