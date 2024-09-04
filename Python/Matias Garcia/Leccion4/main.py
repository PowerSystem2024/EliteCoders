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

#Repaso de set 
#Para definir un conjunto
conjunto2=set()
conjunto1={'bye',}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
#Preguntamos si el num 3 esta en el set
print(3 not in conjunto1)

#Como hacer la igualdad de dos conj
print(conjunto1==conjunto2)#respuesta boolean

#Operaciones en conjuntos
#Agregando varios set en uno
conjunto3= conjunto1 | conjunto2
print(conjunto3)

#CON esto imprimimos el valor que esta en ambos sets
conjunto3= conjunto1 & conjunto2
print(conjunto3)

#Asigna el valor que esta en el set 1 y no en el 2
conjunto3= conjunto1 - conjunto2
print(conjunto3)
conjunto3= conjunto2 - conjunto1
print(conjunto3)

#Elementos que no comparten o que son diferentes entre ambos
conjunto3= conjunto1 ^ conjunto2
print(conjunto3)

conjunto3= conjunto1 | conjunto2
#Aqui preguntamos si un set es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

#Preguntemos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issubset(conjunto1))#si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto3.issubset(conjunto2))
print(conjunto2.issubset(conjunto3))


#como savar si ambos conjuntos son disconexos, est0 es si no comparten alementos en comun
print(conjunto1.isdisjoint(conjunto2))#No hay en comun

#Convertir un conjunto totalmente en inmutable
conjunto1=frozenset#Esto hace que el concunto sea inmutable
#No se puede agregar, modificar ni eliminar elementos del conjunto

#Repaso Diccionarios
diccionarionuevo={'Azul':'Blue','Rojo':'Red','Verde':'Green','Amarillo':'Yellow'}
print(diccionarionuevo)

#Como eliminar
#del (diccionarioNuevo['Azul'])
print(diccionarionuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2={'Matias':{'Edad':18,'Altura':1.83},'Lucia':[45,1.89],'Natalia':[25,1.67]}
print(diccionario2)


#DICCIONARIO DE LA SELECCION ARGRENTINA(Peso,altura y demas estimado"Lo importante es paracticar no?")
selecionArgentina= {
    10:{'Nombre':'Lionel Messi','Edad': 35,'Altura':1.70,'Precio':'50 millones','Posocion':'Extremo derecho'},
    11:{'Nombre':'Dimaria','Edad': 37,'Altura':1.85,'Precio':'20 millones','Posocion':'Centro derecho'},
    24:{'Nombre':'Otamendi','Edad': 36,'Altura':1.81,'Precio':'10 millones','Posocion':'supeirorderecho'},
    19:{'Nombre':'Julian Alvarez','Edad': 31,'Altura':1.79,'Precio':'45 millones','Posocion':'superior derecho'},
    5:{'Nombre':'Cuti Romero','Edad': 34,'Altura':1.83,'Precio':'40 millones','Posocion':'inferior derecho'},
    7:{'Nombre':'Paredes','Edad': 32,'Altura':1.80,'Precio':'80 millones','Posocion':'Centro izquierdo'},
    9:{'Nombre':'Lochelso','Edad': 30,'Altura':1.81,'Precio':'60 millones','Posocion':'Extremo Izquierdo'},
    1: {'Nombre':'Dibu Martinez','Edad': 36,'Altura':2.00,'Precio':'40 millones','Posocion':'Arquero'} ,  
    4: {'Nombre':'Molina','Edad': 25,'Altura':1.90,'Precio':'45 millones','Posocion':'Estremo derecho'} ,
}

for llave,valor in selecionArgentina.items():
    print(llave,valor)

#Como tarea agregar por lo menos 4 jugadores al diciionario(Ya hecho)
print('Tenemos cargados en el diccionario la cantidad de jugadoes: ', end=' ')
print(len(selecionArgentina))

#Pilas usando listas
pila= [1,2,3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado= pila.pop()#Quita el ultimo elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi {pila}')
#Colas con listas 
#Estructura de datos tipos fifo(first input / first output)
cola=['Ariael','Osvaldo','Liliana','Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elemenros de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente:{seRetira}')
print(cola)

#Sacamos elemenros de la cola y imprimimos
seRetira= cola.pop(0)
print(f'Atendido el cliente:{seRetira}')
print(cola)

seRetira= cola.pop(0)
print(f'Atendido el cliente:{seRetira}')
print(cola)

seRetira= cola.pop(0)
print(f'Atendido el cliente:{seRetira}')
print(cola)

seRetira= cola.pop(0)
print(f'Atendido el cliente:{seRetira}')
print(cola)

