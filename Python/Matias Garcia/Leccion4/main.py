#Listas
#COLECCIONES EN PYTHON

#LAS LISTAS SE LAS CONOCE COMO ARREGLOS O VECTORES
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
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
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

#TIPO SET
planetas={"Martes","jupiter","venus"}
print(len(planetas))

#REVISAR UN ELEMENTO SI EXISTE EN EL SET
print("Martes" in planetas)

#AREGAR UN ELEMENTO 
planetas.add("Tierra")# add 
print(planetas)

#ELIMINAR UN ELEMENTO
planetas.remove("Martes")
print(planetas)

#ELIMINAR UN ELEMENTO SIN DISTINCION DE MAYUSCULAS/ MINUSCULAS
planetas.discard("Tierra")
print(planetas)

#LIMPIAR SET
planetas.clear()
print(planetas)

#ELIMINAR SET
#del planetas
#print(planetas)

#DICCIONARIOS
#"Maradona": 10 un diccionario esta compuesto por dos elementos
#UNA LLAVE Y UN VALOR
#dic(key, value)

diccionariao={
    'IDE':'Integrated Develoment Environment',
    'POO':'Programacion orientada a objetos',
    'SABD':'Sistema de administracion de Basse de Datos',           
              
}

#Verificar la cantidad de elementos del diccionario
print(len(diccionariao))
print(diccionariao)

#ACCEDR A UN DICCIONARIO CON LA LLAVE (KEY)
print(diccionariao["IDE"])

#OTRA FOTMA DE RECUPERAR UN ELEMENTO
print(diccionariao.get('POO'))
print(diccionariao.get('SABD'))

#MODIFICAMOS ELEMENTOS
diccionariao['IDE'] ='Entorno de desarrollo integrado'
print(diccionariao)

#COMO RECORRER LAS KEYS
for termino in diccionariao:
    print(termino)

#PARA RECORRER AMBOS VALORES
for termino,valor in diccionariao.items():
    print(termino,valor)
    
#COMO RECORRER LAS KEYS PERO CON FUNCION
for termino in diccionariao.keys():
    print(termino)

#COMO RECORRER LOS VALORES
for valor in diccionariao.values():
    print(valor)

#COMPROBAR LA EXIXTENCIA DE UN ELEMENTO
print('IDE'in diccionariao)

#AGREGAR UN ELEMENTO
diccionariao['PK']='Primary key'
print(diccionariao)

#ELIMINAR UN ELEMENTO
diccionariao.pop('SABD')
print(diccionariao)

#VACAR UN DICCIONARIO
diccionariao.clear()
print(diccionariao)

#ELIMINAR DICCIONARIO
#del diccionariao #se elimino
print()

#CONCATENAMOS LISTAS
lista1=[1,2,3,1]
lista2=[4,5,6,1]
lista3=lista1+lista2 #concatenamos
print(lista3)

#FUNCION PARA AGREGAR VARIOS ELEMENTOS A UNA LISTA
lista3.extend([7,8,9,1])
print(lista3)

#FUNCION PARA UBICAR EN QUE INDICE ESTA EL VALOR INGRESADO
print(lista3.index(5))
#ESTO DARIA ERROR
#print(lista3.index(0))

#COMO SAVER CUANTOS VALORES REPETIDOS HAY EN LA LISTA
print(lista3.count(1))#cuenta cuantos valores iguales hay dentri de la lista

#PARA IMPRIMIR AL REVES LA LISTA
lista3.reverse()
print(lista3)

#Para que se multipliquen los elementos de una lista
lista3=lista3*2
print(lista3)

#Metodos de ordenamiento, en python es una funcion
lista3.sort()#ordena los elementos asendentemente
print(lista3)
#aqui desendentemente
lista3.sort(reverse=True)
print(lista3)

#Repaso de tuplas
tupla=(4,'HOLA',6.78,[1,2,78],4,'Hola')#diferentes tipos de datos
print(tupla)

#Accion booleana, por su repuesta
#En duplas se puede usar : index, count, len
#En tuplas se puede convertir se tupla a lista y de lista a tupla
print(4 in tupla)
