#Ejercicio 8: Menu interacitivo - Cajero Automatico
#hacer un programa que simule un cajero automatico con un slado inicial de $1000 y tendra el siguiente menu de opciones:
#1.Ingresar dinero a la cuenta
#2.Retirar dinero de la cuenta
#3.Mostrar dinero disponible
#4.Salir

Dinero = 1000
opcion = 0
while opcion != 4:
    print('Seleccionar una de las siguientes opciones:')
    print('1. Ingresar dinero')
    print('2. Retirar dinero')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Ingresa la opcion deseada: '))
    print('\n')
    if opcion == 1:
        Dinero = Dinero + (int(input('Ingresa la cantidad de dinero que deseas depositar: ')))
        print('\n')
    elif opcion == 2:
        Dinero = Dinero - (int(input('Ingresa la cantidad de dinero que deseas retirar: ')))
        print('\n')
    elif opcion == 3:
        print('La cantidad de dinero disponible es: ', Dinero)
        print('\n')
    elif opcion == 4:
        print('Gracias por usar el cajero automatico\n')
    else:
        print('La opcion ingresada no es valida\n')