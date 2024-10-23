#Ejercicio 3: Funcion recursiva
#Imprimir numeros de 5 a 1 de manera descendete usando funciones recursivas
#Pede ser culaquier valor positivo, por ejemplo, si pasamos el
#valor 5, imprimira 5,4,3,2,1.

def descendente(num):
    if num >0:
        print(num)
        descendente(num-1)

descendente(int(input('Ingresa un numero: ')))