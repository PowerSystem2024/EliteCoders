#Ejercicio 7: Juego adivina el numero
#Realizar un juego para adivinar el numero. Para ello se debe
#generar un numero aleatorio entre 1 y 100. y luego ir pidiendo
#numeros indicando si es mayor o menor con respecto a n. El proceso
#termina cuando el usuario acierta y alli se mostrara el numero de intentos.


import random

aleatorio = random.randint(1,100)

intentos = 0

while True:
    numero = int(input('Ingresa un numero: '))
    intentos += 1
    if numero == aleatorio:
        print(f'Felicidades, adivinaste el numero en {intentos} intentos')
        break
    elif numero < aleatorio:
        print('El numero es mayor')
    else:
        print('El numero es menor')

