#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#elimine los elementos repetidos, por ultimo mostrar la lista.


lista = [1,1,2,2,4,5,5,5,8,9,10,10,10,10,14,15,16,17,18,19,20,22,22,22,24,25,26,27,29,29,30]

sinRepetidos = set(lista)
lista = list(sinRepetidos)

print(lista)
