#Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del senor de los anillos:
# Nombre: Aragorn
# Clase: Guerrero
# Raza: Dunedain

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar


Personaje1 = {"Nombre":"Aragorn","Clase":"Guerrero","Raza":"Dunedain"}
Personaje2 = {"Nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"}
Personaje3 = {"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}

Personaje4 = {"Nombre":"Gimli","Clase":"Guerrero","Raza":"Enano"}
Personaje5 = {"Nombre":"Frodo","Clase":"Explorador","Raza":"Hobbit"}
Personaje6 = {"Nombre":"Sam","Clase":"Explorador","Raza":"Hobbit"}

Personajes = [Personaje1,Personaje2,Personaje3]
Personajes.append(Personaje4)
Personajes.extend([Personaje5,Personaje6])
print(Personajes)
