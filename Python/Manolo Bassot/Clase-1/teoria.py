#Colecciones en Python
#Listas: es lo que conocemos en otros lenguajes como arreglos o vectores

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

nombres.append('Marcelo')#Agrega un elemento al final de la lista
nombres.append ([1,2,3]) #Tambien podemos agregar tuplas dentro de una lista
nombres.append (True) #o valores booleanos
nombres.append (10.45) #o valores decimales
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

#Tipo set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas)) #Imprime la cantidad de elementos, len = length = largo

#Revisar si un elemento se encuentra en el set
print('Marte' in planetas) #Devuelve True o False

#Agregar un elemento
planetas.add('Tierra') #Agrega un elemento
planetas.add('Tierra') #No se agrega el elemento porque ya existe
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Tierra')
print(planetas)
planetas.discard('Tierra') #No arroja un error si el elemento no existe
print(planetas)

#Limpiar un set
planetas.clear()
print(planetas)

#Borrar un set
del planetas

#Un diccionario esta compuesto por 2 elementos: clave y valor
#dict = {clave:valor}
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
#Verificar la cantidad de elementos
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la key
print(diccionario['IDE']) #La KEY tiene que estar ecrita exactamente igual que como fue ingresada

#Otra forma de acceder a un diccionario
print(diccionario.get('POO'))

#Modificar un elemento
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorrer los elementos
for termino in diccionario: #Muestra solo las llaves
    print(termino)

#Necesitamos una funcion para reccorer los elementos
for termino, valor in diccionario.items(): #Muestra las llaves y los valores
    print(termino, valor)

#Otras maneras de acceder al diccionario
for termino in diccionario.keys(): #Muestra solo las llaves
    print(termino)

for valor in diccionario.values(): #Muestra solo los valores
    print(valor)

#Comprobar si existe una key
print('POO' in diccionario)

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Limpiar un diccionario
diccionario.clear()
print(diccionario)

#Borrar un diccionario
del diccionario

#Concatenacion de listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7,8,9])#Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Funcion para saber en que indice se encuentra un elemento
#Si el elemento no se encuentra, arroja un error

#Como saber cuantos veces se repite un elemento
print(lista3.count(1))

#Invertir el orden de la lista
lista3.reverse()
print(lista3)

#Multiplicar la lista reptiendo sus elemnetos
lista3 =lista3 * 2

#Metodos de ordenamiento, en python es una funcion
lista3.sort() #ordena los elementos de menor a mayor
print(lista3)
lista3.sort(reverse=True) #ordena los elementos de mayor a menor
print(lista3)

#Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1,2,78], 4, 'Hola', 6.78, [1,2,78]) #Puede tener varios tipos de datos
print(tupla)

print(4 in tupla) #Comprobar si un elemento se encuentra en la tupla
#Lo que podemos usar dentro de tuplas son: index, count, len.
