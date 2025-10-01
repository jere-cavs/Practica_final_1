Jugador_1 = input("Ingrese el nombre del jugador 1: ")
Jugador_2 = input("Ingrese el nombre del jugador 2: ")

Inicio1 = input("Que elije Jugador 1?, ¿Piedra, Papel o Tijeras?: ")
Inicio2 = input("Que elije Jugador 2?, ¿Piedra, Papel o Tijeras?: ")

Primer_caso = Jugador_1 == "Papel" and Jugador_2 == "Piedra"
Segundo_caso = Jugador_1 == "Tijeras" and Jugador_2 == "Papel"
Tercer_caso = Jugador_1 == "Tijeras" and Jugador_2 == "Papel"
Cuarto_caso = Jugador_1 == "Piedra" and Jugador_2 == "Piedra"
Quinto_caso = Jugador_1 == "Papel" and Jugador_2 == "Papel"
Sexto_caso = Jugador_1 == "Tijeras" and Jugador_2 == "Tijeras"
Igualdad = Cuarto_caso or Quinto_caso or Sexto_caso

Intentos = 0
Intentos_max = 3

while Intentos < Intentos_max:
    if Igualdad:
        print("¡Empate!")
    elif Jugador_1 == Primer_caso or Segundo_caso or Tercer_caso:
        print("Ha ganado", Jugador_1)
    else:
        print("Ha ganado", Jugador_2)
        break

Intentos += 1