# Listas: Conjunto de elementos - nombres. Ej: Liliana, Osvaldo, Marina. Cada indice es un elemento

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0]) # para ver un unico elemento
print(nombres[1])
print(nombres[-1]) #muestra el ultimo
print(nombres[-1])

print(nombres[0:2]) #recorre una cantidad de indices

# ir del inicio de la lista al indice (sin incluirlo

print(nombres[ : 3]) #0, 1 y 2, el vacio ya indica el 0

#Desde el indice indicado hasta el final

print(nombres[1: ])

#Modificar un valor en la lista

nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

#Iterar una lista

for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene

print(len(nombres)) #le pasamos como parametros a la funcion la lista

#Agregar elementos a la lista

nombres.append('Marcelo') #Se agrega al final
print(nombres)

#Insertar nuevo elemento en u indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminar un elemento

nombres.remove('Alberto')
print(nombres)

#Eliminar el ultimo elemento
nombres.pop() #borra el ultimo de la lista, no el ultimo ingresado
print(nombres)

#Eliminar un indice especifico
del nombres[2]
print(nombres)

# Eliminar, borrar o limpiar todos los elementos

nombres.clear()
print(nombres)

#Eliminar la lista

del nombres
print(nombres) #error, pues no existe
