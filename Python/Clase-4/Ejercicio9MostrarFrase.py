#Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
#Hacer un programa donde el ususario ingrese una frase, se le 
#devolvera la misma frse pero sin espacios en blanco, y 
#ademas un contador de cuantos caracteres tiene la frase.
#(sin contar los espacios en blanco)

frase = input('Ingresa una frase: ')

frase = frase.replace(' ','')

print(frase)

print(len(frase))