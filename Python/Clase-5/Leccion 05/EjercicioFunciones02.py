#Ejercicio 2: Funcion con * args para multiplicar
#crear una funcion para multiplicar los valores recibidos
#de tipo numerico, utilizando argumentos varuabkes *args
#como parametro de la funcion y regresar como resultado
#la multiplicacion de todos los valores pasados como argumento

#Definimos la funcion para multiplicar
def multiplicar_valores(*numeros):
    resultado=1#EL cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado*=numero
    return resultado
#LLamamos la funcion 
print(multiplicar_valores(3,5,15))#Le pasamos argumentos

