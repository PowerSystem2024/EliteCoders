#Ejercicio 11: Agenda telefonica
#Hacer un programa que simule una agenda de contactos.Crear un
#diccionario donde la clave sea el nombre del usuario y el valor 
#sea el telefono, debe tener el siguiente menu
#1.Nuevo contacto
#2.Borrar contacto
#3.ver contactos existentes
#4.salir

#creo un diccionario 
diccContactos={}
#Imprimo las 4 opciones y le pido al usario que digite alguna
print("1.Nuevo contacto")
print("2.Borrar contacto")
print("3.ver contactos existentes")
print("4.salir")
digitar=int(input("Digite la opcion deseada: "))
#Creo un bucle con 20 intentos para que digite y aga lo necesario
for i in range(20):
    #Segun la opcion que digito anteriormente va entrar en los condiconales siguientes
    if digitar==1:
        #imprimo, pido el nombre del contacto y el numero y luego agrego al diccionario
        print("NUEVO CONTACTO")
        nombreContacto=input("Digite el nombre del Contacto: ")
        numeroContacto=int(input("Digite el numero del Contacto: "))
        diccContactos[nombreContacto]=numeroContacto
        print(f"Agrego a {diccContactos}")
    
    elif digitar==2:
        #Imprimo los valores del diccionario y pregunto el contacto a eliminar
        print("ELIMINAR CONTACTO")
        print(f"Los valores del diccionario son: {diccContactos}")
        eliminarContacto=input("Digite el nombre del Contacto a Eliminar: ")
        #Luego elemino el contacto en la lista y imprimo como quedo el resultado
        del diccContactos[eliminarContacto]
        print(f"Los valores del diccionario ahora son: {diccContactos}")
    
    elif digitar==3:
        #Creo un bucle que recorrar los valores y las llaves y que imprima los contactos
        for i in diccContactos.items():
            print(f"Los contactos existente son:\n {i}")
    
    elif digitar==4:
        #Sale del bucle y finaliza
        break


    #Cada ves que sale de un condicional, menos el ultimo, va a ejecutar esto para nueva opcion    
    print("1.Nuevo contacto")
    print("2.Borrar contacto")
    print("3.ver contactos existentes")
    print("4.salir")
    digitar=int(input("Digite la opcion deseada: "))
#finaliza    
print("Finalizo")