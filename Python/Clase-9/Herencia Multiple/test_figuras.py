from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica
print("Creacion del objeto clase Cuadrado".center(50,"_"))
cuadrado1 = Cuadrado(8, 'celeste')
cuadrado1.alto= 7
#cuadrado1.ancho=7

#print(f'Alto: {cuadrado1.alto}')
#print(f'Ancho: {cuadrado1.ancho}')
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')
print(f'Color: {cuadrado1.color}')

print(f'\n{cuadrado1}')
print("Creacion del objeto clase Rectangulo".center(50,"_"))
rectangulo1 = Rectangulo(3, 9, 'violeta')
rectangulo1.ancho=8
print(f'\nCálculo del área del rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)


#figura1=FiguraGeometrica()No SE PUEDE INTANCIAR, ES ABSTRACTA


print(Cuadrado.mro())
