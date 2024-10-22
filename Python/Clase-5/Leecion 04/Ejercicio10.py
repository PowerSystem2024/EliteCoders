#Ejercicio 10:No repetir caracteres
#Hacer un programa que pida una cadena por teclado, lurgo
#Meter los caracteres en una lista sin repetir caracteres
#Autor [EliteCoders]

#Creamos una lista y pedimos al usuario
lista=[]
palabra= input("Digite una palabra: ") 
#Creamos un for para recorrer la palabra
for i in palabra:
    #Si no esta repetida en la lista entonces agrego a la lista
    if i not in lista:  
        lista.append(i)
#imprimo        
print(f"\nLista final sin repeticion: \n {lista}")

