#Comenzamos con funciones
#mi_funcion() no se puede llamara antes de definirla
#Definimos una funcion

def mi_funcion():#Para identificar a la funcion utilizamos parentesis
    print('Saludos a todos los alumnos de la tecnicatura')

mi_funcion()#Estamos llamando a la funcion
mi_funcion()#Se puede llamar N cantidad de veces

#Desempaquedato de lista o lis Umpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ['Ariel', 'Betancud']
show(person[0], person[1])#Pasamos uno por uno los datos de la lista a la funcion
show(*person)#Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ('Osvaldo', 'Giordanini') #Desempaquetamos a travez de un tupla
show(*person2)
person3 = {'name': 'Lucero', 'lastName': 'Natalia'}
show(**person3)

numbers = [1, 2, 3, 4, 5]# Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break#Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se termino')

#List comprehension, lista de comprension
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P'] #esto regresa una nueva lista
print(alongP)

bottleC = [{'name': 'Quilmes', 'country': 'Argentina'},
           {'name': 'Corona', 'country': 'Mexico'},
           {'name': 'Stella Artois', 'country': 'Belgium'}]

Arg = [b for b in bottleC if b['country'] == 'Argentina']
print(Arg)
print(bottleC)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print('Saludos a todos los que ven a traves del canal de YouTube')
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

#La palabar return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a=0, b=0):#Le damos un valor por defecto
    return a + b
resultado = sumar2()
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar2(22, 66)}')

#Argumentos, variables en funciones
def listarNombres(nombres):#Normalmente se utiliza: *args
    for nombre in nombres:#Se va a convertir en una tupla
        print(nombre)
#listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
#listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos):#Normalmente se utiliza: **kwargs
    for llave, valor in terminos.items():#kwargs significa: key word arguments
        print(f'{llave}: {valor}')

listarTerminos()#No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')
listarTerminos(Nombre="Leonel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2= ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10,11) No es un objeto iterable
desplegarNombres((10,11)) #La covertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) #La convertimos a una lista 

#Funciones Recursivas
def factorial(numero):
    if numero == 1:#Caso base
        return 1
    else:#Caso recursivo
        return numero * factorial(numero - 1)
resultado=factorial(5)#Lo hacemos en codigo duro
print(f'El factorial de 5 es: {resultado}')
resultado=factorial(int(input('Ingresa un numero: ')))#Lo hacemos en consola
print(f'El factorial del nuimero ingresado es: {resultado}')