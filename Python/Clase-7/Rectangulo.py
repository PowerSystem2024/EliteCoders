"""
Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
el nombre dle metodo sera calcular area utilizando la formula:
area = base * altura. Pero la base y la altura deben ser ingresados por
el usuario y los objetos deben ser tres.
"""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    
print('Vamos a calcular el area de un rectangulo:')
rectangulo1 = Rectangulo(0,0)
rectangulo1.base = int(input('Ingresa la base: '))
rectangulo1.altura = int(input('Ingresa la altura: '))
print(f'El area del rectangulo es: {rectangulo1.area()}')
