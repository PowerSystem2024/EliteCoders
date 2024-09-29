#Ejercicio: Llenar una lista
#Llenar una lista con los numeros del 1 al 50, luego mostrar 
#la lista con el bucle for.


lista = []

for i in range(1,51):
    lista.append(i)


for i in lista:
    if i<50:
        print(f'{i}-',end='')
    else:
        print(f'{i}')
