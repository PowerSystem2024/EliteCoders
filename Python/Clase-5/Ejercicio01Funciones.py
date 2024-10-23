#Ejercicio 1: Crear una funcion para sumar los valores recibidos de tipo
#numerico, utilizando argumentos variables *args como parametro de la
#funcion y agregar como resultado la suma de todos los valores pasados
#como argumentos.

def sumar_numeros(*args):
    suma = 0
    for i in args:
        suma += i
    return suma


print('La suma de los numeros es: ',sumar_numeros(1, 2, 3, 4, 5))
