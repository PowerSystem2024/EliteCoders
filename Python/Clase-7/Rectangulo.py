class Rectangulo:

    """
    Crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    El nombre del metodo será calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario
    y los objetos deben ser 3
    """

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


base = int(input('Digite el numero de la base: '))
altura = int(input('Digite el numero de la altura: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El área del rectangulo es: {rectangulo1.calcular_area()}')