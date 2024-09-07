#Tipo SET (conjunto) - no tiene orden y no se permite modificar, pero si agregar y eliminar. no hay indice - orden aleatorio

planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) #cuantos caracters

#Revisar si un elemento existe dentro del set
print('Marte' in planetas) #bool - case sensitive
print('Júpiter' not in planetas)

#Agregar un elemento
planetas.add('Tierra')
print(planetas)

#Eliminar elementos (tienen q existir)
planetas.remove('Júpiter')
print(planetas)

planetas.discard('Tierra') #esta no da error case sensitive, per ono lo elimina
print(planetas)

#Limpiar set

planetas.clear()
print(planetas)

#Eliminar set
del planetas

#Diccionario en Python

#Conjunto de los 2 es el diccionario - una llave y un valor
#dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
print(diccionario)

#Largo de elementos
print(len(diccionario))

#Acceder a un elemento en dict - no hay indice, se accede desde el key
print(diccionario['IDE']) #MUESTRA SOLO EL VALUE

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))

#Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Recorrer elementos
for termino in diccionario:
    print(termino) #muestra llaves

#Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario

for termino in diccionario.keys():
    print(termino) #muestra solo llaves

for valor in diccionario.values():
    print(valor) #muestra solo los valores

#Comprobar la existencia de algun elemento
print('IDE' in diccionario) #Devuelve bool

#Agregar elemento al dic
diccionario['PK'] = 'Primary key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar el diccionario
diccionario.clear()
print(diccionario)

#Eliminar el diccionario
del diccionario

#Concatenar listas

lista1 = [1, 1, 2, 3]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9]) #agregar varios elementos
print(lista3)

print(lista3.index(5)) #donde ubica el valor en el index

#Como saber cuantos valores repetidos hay en la lista
print(lista3.count(1))

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

#Metodos de ordenamiento
lista3.sort() #Ordena de manera ascendente
print(lista3)
lista3.sort(reverse=True) #Ordena descendente
print(lista3)

#Repaso Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') #Puede tener diferentes tipos de datos
print(tupla) #bool si existe
#Lo que podemos usar en tuplas: index, count, lenght

print(4 in tupla)
#Otras funciones de las listas (tambien llamadas arreglos o vectores)

#Listas dentro de listas
nombres = ['Ariel', 'Naty']
nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)
