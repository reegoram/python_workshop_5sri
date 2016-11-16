'''
@reegoram
Simular el juego de piedra papel o tijera
'''

#Este import nos permite utilizar una método para generar números aleatorios
from random import randint

posiblesManos = ["Piedra", "Papel", "Tijera"]
termina = False

while termina == False:
    manoIA = randint(1,3) #Generamos un número entre 1 - 3 que representan las posibles manos
    #print("Debug: manoIA = %i" %manoIA) #descomentar para depurar 
    manoJugador = int(input("Indique su mano: \n1.Piedra \n2.Papel \n3.Tijera\n>> "))

    #Error de entrada
    if manoJugador > 3:
        print("Opcion no valida")
    #Empate
    if manoIA == manoJugador:
        print("Empate, ambos tomaron la misma mano")
    #Papel gana a piedra
    if manoIA == 1 and manoJugador == 2:
        print("Gana el jugador, porque %s le gana a %s" %(posiblesManos[manoJugador - 1], posiblesManos[manoIA - 1]))
    if manoIA == 2 and manoJugador == 1:
         print("Gana la IA, porque %s le gana a %s" %(posiblesManos[manoIA - 1], posiblesManos[manoJugador - 1]))
    #Tijera gana a papel
    if manoIA == 2 and manoJugador == 3:
        print("Gana el jugador, porque %s le gana a %s" %(posiblesManos[manoJugador - 1], posiblesManos[manoIA - 1]))
    if manoIA == 3 and manoJugador == 2:
         print("Gana la IA, porque %s le gana a %s" %(posiblesManos[manoIA - 1], posiblesManos[manoJugador - 1]))
    #Piedra gana a Tijera
    if manoIA == 3 and manoJugador == 1:
        print("Gana el jugador, porque %s le gana a %s" %(posiblesManos[manoJugador - 1], posiblesManos[manoIA - 1]))
    if manoIA == 1 and manoJugador == 3:
         print("Gana la IA, porque %s le gana a %s" %(posiblesManos[manoIA - 1], posiblesManos[manoJugador - 1]))
    
    print("\n")
    respuesta = str(input("¿Jugar otra vez? (S/N)"))
    if respuesta != "S":
        termina = True