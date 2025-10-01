Intentos = 0
Intentos_max = 3

Nombre_1 = input("Ingrese el nombre del jugador 1: ")
Nombre_2 = input("Ingrese el nombre del jugador 2: ")

while Intentos < Intentos_max:

    Jugador1 = input("Que elije Jugador 1?, ¿Piedra, Papel o Tijeras?: ").lower()
    Jugador2 = input("Que elije Jugador 2?, ¿Piedra, Papel o Tijeras?: ").lower()

    Primer_caso = (Jugador1 == "Piedra" and Jugador2 == "Tijeras")
    Segundo_caso = (Jugador1 == "Papel" and Jugador2 == "Piedra")
    Tercer_caso = (Jugador1 == "Tijeras" and Jugador2 == "Papel")

    if Jugador1 == Jugador2:
        print("¡Hay un EMPATE!")

    elif (Primer_caso) or (Segundo_caso) or (Tercer_caso):
        print("Ha ganado: ", Nombre_1)

    else:
        print("Ha ganado: ", Nombre_2)
    
    Intentos += 1