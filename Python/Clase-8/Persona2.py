class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # Decorador
    def nombre(self):  # Metodo getter
        #        print('Estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo setter
        #        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property  # decorador para apellido
    def apellido(self):  # Metodo getter para apellido
        #        print('Utilizando el metodo get para apellido')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo setter para apellido
        #        print('Utilizando el metodo set para apellido')
        self._apellido = apellido

    @property  # decorador de edad
    def edad(self):  # metodo getter para edad
        #        print('Utilizando el metodo get para edad')
        return self._edad

    @edad.setter
    def edad(self, edad):  # metodo setter para edad
        #        print('Utilizando el metodo set para edad')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    Persona1 = Persona2('Alex', 'Montenegro', 22)
    print(Persona1.nombre)  # Llamamos al metodo getter
    Persona1.nombre = 'Martin'  # llamamos al metodo setter
    print(Persona1.nombre)  # otra vez con el metodo getter
    print(Persona1.mostrar_detalles())  # llamamos el metodo mostrar_detalles
    # Atributo read-only sería la edad porque no tiene el metodo set
    print(Persona1.edad)

    # Tarea crear tres objetos mas, utilizando los metodos getter and setter
    # para modificiar, y mostrar los cambios con el metodo mostrar_detalles

    #Primer Objeto de la tarea
    persona2 = Persona2('Felix', 'Marin', 30)
    persona2.nombre = 'Marcos'
    persona2.apellido = 'Martinez'
    persona2.edad = 31
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())

    #Segundo objeto de la tarea
    persona3 = Persona2('Monica', 'Lucero', 58)
    persona3.nombre = 'Martina'
    persona3.apellido = 'Branca'
    persona3.edad = 60
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    #Tercer objeto de la tarea
    persona4 = Persona2('Capital', 'Cordoba', 66)
    persona4.nombre = 'Carlos'
    persona4.apellido = 'Corbalan'
    persona4.edad = 71
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalles())

    print(__name__)
