class Persona:#Creamos una clase
    #pass #No se procesa nada mas (No tiene contenido)
    def __init__(self, nombre, apellido,dni, edad, *args, **kargs): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #_ para encapsulamiento (no se puede cambiar) si es __ esta prohibido
        self.edad = edad
        self.args = args
        self.kargs = kargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}. La dirección es {self.args}. '
              f'Los datos importantes son: {self.kargs}')

#print(type(Persona))
persona1 = Persona('Ariel', 'Perez', 4043434343434, 40) #Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1._dni)
print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre}{persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 4543434334, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre}{persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre}{persona1.apellido} Su edad es: {persona1.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() #La referencia se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) #Debemos pasar referencia al self o tira error

persona1.telefono = '4445599'
print(f'Este es el teléfono de : {persona1.nombre} {persona1.telefono}') #Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene atributo, da error

persona3 = Persona('Rogelio', 'Romero', 229863456, 22, 'Teléfono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo='2021')
persona3.mostrar_detalle()

# print(persona3._dni) #esto no se puede utilizar (está encapsulado), mala practica en py

# persona3.__nombre #Está totalemnte encapsulado