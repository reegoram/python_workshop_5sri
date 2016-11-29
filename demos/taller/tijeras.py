from random import randint

posiblesManos = ["Piedra", "Papel", "Tijera"]

print("Escoja una mano \n1. Piedra \n2. Papel \n3. Tijera")
manoJugador = int(input())

manoIA = randint(1,3)
print("Debug: manoIA = %i" %manoIA) #Sólo para saber que eligio IA

if manoJugador > 3:
    print("Opcion no valida")
else:

    #Comparar la manoIA con la manoJugador
    if manoJugador == manoIA:
        print("Empate")
    else:
        if manoIA == 1 and manoJugador == 2:
             print("Gano el jugador")
        if manoIA == 2 and manoJugador == 1:
             print("Gano la maqima")
        if manoIA == 2 and manoJugador == 3:
             print("Gano el jugador")
        if manoIA == 3 and manoJugador == 2:
             print("Gano la maqima")
        if manoIA == 3 and manoJugador == 1:
             print("Gano el jugador")
        if manoIA == 1 and manoJugador == 3:
             print("Gano la maqima")