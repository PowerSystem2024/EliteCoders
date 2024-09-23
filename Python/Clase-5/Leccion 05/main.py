#Funciones
#Bloque de codigo reutilizable
def mi_funcion():
    print("Hola que tal")
#Llamo a la fucion
mi_funcion()

#Desempaquetado de listas Unpaquin

#Creo una funcion con dos parametros
def show(name, lastname):
    print(name+" "+lastname) #imprimo 
person=["Matias","Garcia"]#creo una lista con nombre y  apllido
#Le paso los parametros a la funcion con los indices de la lista
show(person[0],person[1])
#llamo a la funcion
show(*person)
person2=("Matias","Garcia")#creo una tupla con nombre y  apllido
show(*person2)#Llamo a la funcion, pero pasandole lso parametros de la tupla person2
#creo un diccionario con  nombre y  apllido
person3={'lastname':'Lucero','name':'Natalia'}
show(**person3)#Llamo a la funcion, pero pasandole los parametros de la diccionario person3

#########################
#creo una lista 
numbers =[1,2,3,4,5]
#Recirro la lista 
for n in numbers:
    print(n)#imprimo los valores
    if n ==3:#salgo del bucle si es 3
        break
else:#termina 
    print("Esto se termino")



#List comprehension, lista dee comprecion
#creo una lista  
name=["Paolo","Patri","Ramiro","Pepe"]
# recorremos la lista de una manera simplifida y busco los valores que empiezan con p en la lista
alongP=[p for p in name if p[0]=="P"]
print(alongP)

#Creo una llista en donde almaceno diccionarios
bottleC=[{"name":"Quilmes","Country":"Arg"},
         {"name":"Corona","Country":"Mx"},
         {"name":"Stella Artois","Country":"Belgium"}
         ]
#creo una nueva lista pero en ella creo la condiccion simplificada y imprimo
Arg=[b for b in bottleC if b["Country"]=="Arg" ]
print(Arg)
print(bottleC)

#Paso de Argumentos(funcion)
def mi_funcion2(name, lastName):
    print("Saludos a todos lo que ven a traves del canal de youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")

mi_funcion2("Ezel","Ozoglu")
mi_funcion2("Paulo","Visintin")
mi_funcion2("Clara","Martinez")

#La palabra return
#Creamos una funcion para sumar
def sumar(a,b):
    return a + b 
resultado =sumar(78, 22)
print(f"El resultado de la suma es: {resultado} ")
print(f"El resultado de la suma es: {sumar(55,45)} ")
 
#Valor por default
def sumar2(a,b):
    return a + b 
#resultado=sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

#Argunmetos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombres)
##Les paso los valores a la funcion        
listarNombres("Lucas","Jose","Claudia","Rosa","Maria")
listarNombres("Pedro","Pepe","Clara","Tomas","Mari")

#Lo mas utilizado es **kwargs para recivir argumentos
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave}:{valor}")
#Llamo a la funcion        
listarTerminos()#No muestra nada
#Le pasamos parametros a la funcion
listarTerminos(IDE='Integrided Develoment Enviroment',PK='Primary key')
listarTerminos(Nombres='Lionel MEssi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombre2=['Tito','Pedro','Carlos']
desplegarNombres(nombre2)
desplegarNombres('Carla')
#desplegarNombres(10,11)#No es un objeto iterable
desplegarNombres([10,11])#La convertimos a una tupla, en un solo elemento
desplegarNombres([22,15])

#Funciones Recursivas
def factorial(numero):
    if numero==1:#Caso Base
        return 1
    else:
        return numero*factorial(numero-1)#Caso recursivo

resultado=factorial(5)
print(f"El factorial del numero 5 es: { resultado}")

#Tarea que el usuario ingrese el numero par calcular el factorial
#(HECHO)
#Pido al usuario que digite el numero
num= int(input("Digite un numero par sacar el factorial: "))
#creo la funcion para sacar el factorial
def factorial(numero):
    if numero==1:#Caso Base
        return 1
    else:
        return numero*factorial(numero-1)#Caso recursivo

#almaceno en una variable el valor ya calculado por la funcion y imprimo
calculo=factorial(num)
print(f"El factorial del numero 5 es: { calculo}")