#Listas: 

nombres = ['Naty','Osvaldo','Lily','Ariel']

#Formas de mostrar o llamar uno o varios elemnetos de la lista

print(nombres) #Imprime toda la lista
print(nombres[0]) #Imprime la posicion indicada unicamente
print(nombres[1])
print(nombres[2])
print(nombres[3])

print(nombres[-1])# Con el signo menos se invierte la lista
print(nombres[-2])# y impime de atras hacia adelante

print(nombres[0:2]) #Solo muestra la posicion 0 y 1
print(nombres[:3]) #Muestra desde el principio de la lista hasta la posicion 2 o la que le indiquemos
print(nombres[1:]) #Muestra desde la posicion 1 o la que le indiquemos hasta el final

#Fomrma de modificar un elemento de la lista

nombres[0] = 'Natalia'
print(nombres)

#Iteracion de listas

for nombre in nombres:
    print(nombre)
#else:
    #print('Se acabaron los elementos de la lista')

#Como saber cuantos elementos tiene una lista

print(len(nombres))

# Formas de agregar elementos a la lista

nombres.append('Marcelo') #Agrega un elemento al final de la lista
print(nombres)

nombres.insert(1,'Alberto') #Agrega un elemento en una posicion especifica
print(nombres)

#Formas de eliminar elementos de la lista

nombres.remove('Alberto') #Elimina el dato que le indiquemos
print(nombres)

nombres.pop() #Elimina el ultimo elemento de la lista
print(nombres)

nombres.pop(0) #Elimina el elemento en la posicion que le indiquemos
print(nombres)

del nombres[2] #Elimina el elemento en la posicion que le indiquemos
print(nombres)

#Forma de limpiar una lista

nombres.clear()
print(nombres)

#Forma de borrar una lista

#del nombres
print(nombres)

#Tuplas

cocina = ('cuchara','cuchillo','tenedor')
print(cocina)

#Las funciones para leer las tuplas se pueden realizar de la misma forma que las listas
#(print(cocina), print(cocina[0]), print(cocina[-1]), print(cocina[:2]), print(cocina[1:]))
#la diferencia es que las tuplas no se pueden modificar

#Para que se considere tupla, minimamente se necesita una coma al final del elemento(si es que solo vamos a colocar un elemento)
#Ejemplo:
verduras = ('papa',)

#Forma para evitar el salto de linea en la iteracion
for cocinar in cocina:
    print(cocinar, end=' ')#la funcion end=' ' evita el salto de linea

#Como modificar una tupla

cocinaLista = list(cocina)  #Convertimos la tupla en lista
cocinaLista[0] = 'Plato'    #Modificamos la lista
cocina = tuple(cocinaLista) #Convertimos la lista en tupla
print('\n',cocina) #\n es un salto de linea

#Esta conversion no es una buena practica