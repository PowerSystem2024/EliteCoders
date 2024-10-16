"""
Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
un metodo calcular_volumen que tendra la formula:
volumen = ancho * alto * profundidad
que el usuario ingrese los valores.
"""

class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def volumen(self):
        return self.ancho * self.alto * self.profundidad
    
print('Vamos a calcular el volumen de un cubo:')
cubo1 = Cubo(0,0,0)
cubo1.ancho = int(input('Ingresa el ancho: '))
cubo1.alto = int(input('Ingresa el alto: '))
cubo1.profundidad = int(input('Ingresa la profundidad: '))
print(f'El volumen del cubo es: {cubo1.volumen()}')