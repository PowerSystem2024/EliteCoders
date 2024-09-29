#Ejercicio 11 : Agenda telefonica
#Hacer un programa que simule una agenda de contactos. Crear un
#diccionario donde las claves sean el nombre del usuario y el valor
#sea el telefono.

print('Bienvenido a su agenda telefonica')

opcion = 0
agenda = {}

while opcion != 4:
    print('Elija una de las siguientes opciones')
    print('1. Agregar contacto')
    print('2. Buscar contacto')
    print('3. Eliminar contacto')
    print('4. Salir\n')

    opcion = int(input('Opcion: '))

    if opcion == 1:
        print('\nIngrese el nombre del contacto:')
        nombre = input()
        if nombre in agenda:
            print('\nEl contacto ya existe\n')
        else:
            print('Ingrese el telefono del contacto:')
            telefono = input()
            agenda.update({nombre:telefono})
            print('\nContacto guradado\n')

    elif opcion == 2:
        print('\nIngrese el nombre del contacto:')
        nombre = input()
        if nombre not in agenda:
            print('\nNo se encontro el contacto\n')
        else:
            print (f'\nEl telefono de {nombre} es: ', agenda.get(nombre),'\n')

    elif opcion == 3:
        print('\nIngrese el nombre del contacto:')
        nombre = input()
        if nombre not in agenda:
            print('\nNo se encontro el contacto o ya fue borrado\n')
        else:
            agenda.pop(nombre)
            print('\nContacto eliminado\n')

    elif opcion == 4:
        print('\nHasta luego')
        break