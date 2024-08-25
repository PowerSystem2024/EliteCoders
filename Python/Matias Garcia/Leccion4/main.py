#Listas

nombres=["Naty","Pepo","Martin","Manuel"]

print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
#Determinados indice hasta 2
print(nombres[0:2])
#Hasta el indice 3
print(nombres[ :3])
#De 1 hasta el final
print(nombres[1: ])
#Modificamos el valor 
nombres[2]= "Elon"
nombres[0]= "Maty"
print(nombres)

#Recorrer la lista
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Para saber cuantos elemntos tienen una lista
print(len(nombres))

#agregamos un elemento 
nombres.append("Marcelo")
print(nombres)

#Agregamos un elemento  en un lugar determinado
nombres.insert(3,"Miriam")
print(nombres)
nombres.insert(4,"Mia")
print(nombres)

#ELIMINAMOS UN ELEMENTO DE LA LISTA

# nombres.remove("Mia")
# print(nombres)


#ELIMINAMOS EL ULTIMO ELEMENTO
# nombres.pop()
# print(nombres)

# Eliminar un indice especifico

del nombres[2]
print(nombres)

#BORRAR TODOS LOS ELEMENTOS

# nombres.clear()
# print(nombres)

# Eliminar lista

del nombres[3]
print(nombres)


#Creamos una dupla 

cocina=("cuchara","plato","cuchillo")
print(len(cocina))    

#Acceder a un elemento especif
    
#Acceder a un elemento con corchetes

print(cocina[0])

# mostrar de manera inversa
print(cocina[-1])

#EJEMPLO
verduras= ("papa",)

#Recorremos una dupla
for cocinar in cocina:
    #esto sirve para que se imprima en una misma linea
    print(cocinar, end=" ")


#Para agregar una lista a la tupla
#convierto a lista y luego a tupla
cocinaLista= list(cocina)
cocinaLista[0]="Plato"
cocina= tuple(cocinaLista)
print("\n", cocina)

#Eliminar la tupla++
# del cocina
# print(cocina)





