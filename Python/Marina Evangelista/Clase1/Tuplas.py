#Tupla no se pueden modificar elementos - inmutables - append insert y remove no se pueden usar

#Definimos una tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

#Como acceder a un elemento = corchetes, no parentesis

print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])

#Como acceder a un rango

print(cocina[0:2])

#Ejemplo
verduras = ('papa') #esto es una cadena, no tupla - siempre tiene q tener coma, aunque tenga solo 1 elemento

#Recorrer elementos de una tupla

for cocinar in cocina:
    print(cocinar, end=' ') #usa el \n para los saltos de linea por default. el end es para finalizar con espacio

#Como modificar la tupla(no es best practice)

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

del cocina # la elimina
