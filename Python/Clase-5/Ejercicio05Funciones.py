#Ejercicio 5: Convertidor de temperaturas
#Realizar 2 funciones para convertir de grados celsius
#a farenheit y viceversa. Las formulas son:
#F = (9/5*C) + 32
#C = (5/9)*(F - 32)

def CelToFar(cel):
    far = (9/5)*cel + 32
    print(f'La temperatura {cel}C en Far es: {far}F')

def FarToCel(far):
    cel = (5/9)*(far - 32)
    print(f'La temperatura {far}F en Cel es: {cel}C')

CelToFar(int(input('Ingresar una temperatura en Celsius: ')))
FarToCel(int(input('Ingresar una temperatura en Farenheit: ')))