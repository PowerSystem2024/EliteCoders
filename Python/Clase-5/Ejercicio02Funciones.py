#Ejercicio 2: Funcion con *args para multiplicar
#Crear una funcion para multiplicar los valors recibidos
#de tipo numerico, utilizando argumentos variables *args
#como parametro de la funcion y regresar como resultado
#la multiplicacion de todos los valores pasados como argumentos.

def multi(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado
print('El resultado de la multiplicacion es: ',multi(2,3,4,5))
