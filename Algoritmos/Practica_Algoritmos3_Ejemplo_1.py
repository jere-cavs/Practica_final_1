#Inicio de programa

#Paso 1: Solicitar al usuario que ingrese la edad del cliente
edad_cliente = int(input("Por favor, ingrese su edad: "))

#Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca
permitido = True
if edad_cliente >= 18:
    permitido = True
else:
    permitido = False

# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca
if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, los menores de edad no pueden ingresar a la discoteca")

#Fin del programa