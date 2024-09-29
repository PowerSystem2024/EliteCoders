#Ejercicio 2: Operaciones de conjuntos con listas
#Escriba un programa que tenga 2 listas y que a continuacion
#cree las siguentes listas:(en las que no deben haber elementos repetidos)
# 1) Lista de palabras que aparecen en las listas
# 2) Lista de palabaras que aparecen en la lista 1 pero no en la 2
# 3) Lista de palabras que aparecen en la lista 2 pero no en la 1
# 4) Lista de palabras que aparecen en las dos listas

lista1 = ['Queen','AC/DC','Pink Floyd','Nirvana','Led Zeppelin','AC/DC','Pink Floyd','Nirvana','Led Zeppelin']

lista2 = ['Queen','Nirvana','Black Sabbath','KISS','U2','Queen','Nirvana','Black Sabbath','KISS','U2']

conjunto1 = set(lista1)
conjunto2 = set(lista2)

# 1)

union = list(conjunto1 | conjunto2)
print(f'Las palabras que aparecen en las dos listas son: {union}')
# 2)

lista1 = list(conjunto1 - conjunto2)
print(f'Las palabras que aparecen en la lista 1 pero no en la 2 son: {lista1}')
# 3)

lista2 = list(conjunto2 - conjunto1)
print(f'Las palabras que aparecen en la lista 2 pero no en la 1 son: {lista2}')
# 4)

ambas = list(conjunto1 & conjunto2)
print(f'Las palabras que aparecen en las dos listas son: {ambas}')