import random

numero_secreto = random.randint(0,50)
intentos = 0
cant_max_intentos = 5
adivinado = False

while not adivinado:
    if not intentos < cant_max_intentos:
        print("¡Game Over!, el número ingresado es incorrecto!!!")
        break

    entrada = input("introduce un número del 1 al 50: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicitaciones!, has ganado el juego")
        adivinado = True
    
    elif numero < numero_secreto:
        print("Ingrese un número mayor al ingresado")
    
    else:
        print("Ingrese un número menor al ingresado")
    
    intentos += 1