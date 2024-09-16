#Ejercicio 5: Factorial de un numero positivo
#Hacer un programa que calcule el factorial de un numero positivo

num = int(input('Ingresa un numero positivo: '))

while num < 0:
    num = int(input('El numero debe ser positivo: '))

factorial = 1
for i in range(1,num+1):
    factorial *= i