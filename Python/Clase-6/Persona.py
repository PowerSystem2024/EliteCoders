class Persona:#Creamos una clase
    #pass #No se procesa nada mas (No tiene contenido)
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self):#Self es igual a this
        print(f'La Clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad} {self._dni}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

#print(type(Persona))
persona1 = Persona('Ariel', 'Perez', 32456987, 40) #Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre}{persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre}{persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre}{persona1.apellido} Su edad es: {persona1.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()#La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) Debemos pasarle una referncia para el self o dara error
persona1.telefono = '44445555289'
print(f'Este es el telefono de : {persona1.nombre} {persona1.telefono}')#Hemos creado un atributo de un objeto

# print(prsona2.telefono) el objeto perosna2 no tiene este atriburo, da error
persona3 = Persona('Rogelio', 'Romero', 35789456, 22, 'Telefono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito= 'Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) esto no se debe utilizar en python, esto dice que lo desconocemos
# persona3,__nombre Esta totalmente encapsulado