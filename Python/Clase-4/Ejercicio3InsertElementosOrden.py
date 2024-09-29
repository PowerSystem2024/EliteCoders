#Ejercicio: Insertar elementos en una lista y ordenarlos
#Pedir numeros y meterlos en una lista, cuando el ususario
#introduzca un numero 0, nuestro programa dejaria de insertar.
#Por ultimo, mostrar la lista ordenada de menor a mayor.


lista = []
numero = 1
print("Ingresar numeros a la lista. Para terminar ingresa un 0: ")
while numero != 0:
    numero = int(input('Ingresa un numero: '))
    if numero != 0:
        lista.append(numero)
lista.sort()



print(f'La lista ordenada es: {lista}')
