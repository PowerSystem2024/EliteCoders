#Ejercicio5: convertidor de temperatura
#Realizar dos funciones para convertir de grados celsius
#a fahrenheit y viseversa
#investigar las formulas

#Le doy a elegir opciones y que digite
print("Que quiere calcular?")
print("1.Calcular de Grados centígrados A Grados Fahrenheit ")
print("2.Calcular de Grados Fahrenheit A Grados centígrados ")
opcion=int(input("Digite una opcion: "))

#segun la opcion entra en un condicional y hace el calculo corresponciente
if opcion==1:
    gradosCenti=int(input("Digite los grados celsius: "))
    fahrenheit=(gradosCenti *(9/5)) + 32
    print(f"Sus grados Fahrenheit son: {fahrenheit}")#imprimimos el resultado
elif opcion==2:
    gradosFahrenheit=int(input("Digite los grados celsius: "))
    celsius=(gradosFahrenheit -32) *(5/9) 
    print(f"{gradosFahrenheit} Grados Fahrenheit son: {celsius} Centigrados")#imprimimos el resultado

