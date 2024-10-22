#Ejercicio 01 : Crear una funcion para sumar los valores recibidos de tipo
#numericos, utilizando argumentos variavles *args como parametro de la
#funcion y agregar como resultado la suma de todos lo valores pasados como argumentod
#Definimos la funcion con los parametros que equiera
def sumar_valor(*args):
    resultado=0
    #Ireramos cada elemento, sumamos y retornamos el resultado
    for valor in args:
        resultado+=valor
    return resultado
#imprimo
print(sumar_valor(3,4,5,8,6,8))