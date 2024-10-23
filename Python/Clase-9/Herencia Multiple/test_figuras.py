from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(10, 'celeste')
print(f'Alto: {cuadrado1.alto}')
print(f'Ancho: {cuadrado1.ancho}')
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')
print(f'Color: {cuadrado1.color}')

print(f'\n{cuadrado1}')

rectangulo1 = Rectangulo(10, 20, 'violeta')
print(f'\nCálculo del área del rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)