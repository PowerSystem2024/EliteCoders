#Ejercicio 10: No repetir caracteres.
#Hacer un programa que pida una cadena por teclado , luego
#meter los caracteres en una lista sin repetir caracteres.

frase = input('Ingresa una frase: ')

frase = list(set(frase))

print(frase)