#Ejercicio: Modificar los elementos de una lista
#Llenar una lista con los numeros del 1 al 10, luego modificar
#elementos de lo lista multiplicandolos por un valor ingresado por el usuario.

lista = list(range(1,11))

print(lista)

numero = int(input('Ingrese un valor por el cual quiera multiplicar los elementos de la lista: '))

for i in range(0,10):
    lista[i] *= numero

print(lista)