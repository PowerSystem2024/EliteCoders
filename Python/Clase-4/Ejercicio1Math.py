#Ejercicio 1 matematica: Sacar la raiz cuadrada de un numero

import math

num = int(input('Ingresa un numero: '))

while num < 0:
    num = int(input('El numero ingresado debe ser positivo: '))

print(f'La raiz cuadrada de {num} es: ',math.sqrt(num))
