#Ejercicio 6: Tabla de Multiplicar
#Hacer un programa que pida un numero por teclado y guarde
#en una lista su tabla de multiplicar hasta el 10.

lista = list(range(1,11))
numnero = int(input('Ingresa el numero de la tabla: '))

for i in range(1,11):
    lista[i-1]=numnero*i

print(lista)