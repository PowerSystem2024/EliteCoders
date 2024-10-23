class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre        
        self._apellido = apellido
        self._edad = edad
    
    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property
    def nombre(self):#Metodo Getter
        print('Estamos utilizando el metodo get')
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):#Metodo Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
       self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1._nombre)# Llamamos al metodo getter
    persona1.nombre = 'Juan Pedro'#Llamamos al metodo setter
    print(persona1._nombre)# Llamamos al metodo getter
    print(persona1.mostrar_detalle())# Llamamos el metodo mostrar_detalle
    #Atributo read-only (solo lectura seria la edad porque no tiene el metodo setter)
    print(persona1.edad)

    #Tarea crear 3 objetos mas, utilizando los metoddos getter and setter
    #para modificarlos, y mostrar los cambios con el metodo mostrar_detalle
    print('Tarea crear 3 objetos mas, utilizando los metoddos getter and setter')

    print('Primero Objeto')
    persona2 = Persona2('Liliana', 'Buccella', 40)
    print(persona2.mostrar_detalle())
    persona2.nombre = 'Rosario'
    persona2.apellido = 'Romero'
    persona2.edad = 18
    print(persona2.mostrar_detalle())

    print('Segundo Objeto')
    persona3 = Persona2('Rogelio', 'Romero', 66)
    print(persona3.mostrar_detalle())
    persona3.nombre = 'Carla'
    persona3.apellido = 'Lopez'
    persona3.edad = 22
    print(persona3.mostrar_detalle())

    print('Tercer Objeto')
    persona4 = Persona2('Carlos', 'Lara', 20)
    print(persona4.mostrar_detalle())
    persona4.nombre = 'Luis'
    persona4.apellido = 'Lopez'
    persona4.edad = 18
    print(persona4.mostrar_detalle())

    print(__name__)