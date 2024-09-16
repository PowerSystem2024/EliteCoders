#Ejercicio 4: sumar numeros pares dentro de un rango
# #Hacer un programa para sumar numero pares dentro de un rango 


rango = int(input('Ingresa un rango: '))

lista = list(range(0,rango+1))

suma = 0
for i in lista:
    if i%2 == 0:
        suma += i
print(f'La suma de los elementos pares del rango es: {suma}')