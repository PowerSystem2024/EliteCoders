#Ejercicio 3: funcion recursiva
#Imprimir numeros de 5 a 1 de maneta decendente usando funciones recursivas
#puede ser cualquier valor positivos, eje
#Con 5 debe imprimir
#5
#4
#3
#2
#1
#Si es 3 debe imprimir
#3
#2
#1
#si es negativo numeros negativos no imprime nada
#Que el numero lo ingrese el usuario


#creo la funcion para sacar el factorial
num=int(input("Digite un numero: "))
def numeroRecursivo(num):
    if num>=1:
        print(num)
        numeroRecursivo(num-1)
    elif num==0:
        return
    elif num<=0:
        print("Valor ingresado incorrecto...")    
    
numeroRecursivo(num)
