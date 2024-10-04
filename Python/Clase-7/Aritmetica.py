class Aritmetica:
    """
    El nombre de este tipo de comentario (triple comilla) es DocString
    Esto es documentacionde la CLASE en Python
    Vamos hacer algunas operaciones de: suma, resta, multiplicación y más.
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB # asi empiezan a aparecer

    #Metodo para sumar, restar, multiplicar y dividir
    def sumar(self):
        return self.operandoA+self.operandoB

    def resta(self):
        return self.operandoA-self.operandoB

    def multiplicar(self):
            return self.operandoA*self.operandoB

    def dividir(self):
        return self.operandoA/self.operandoB

aritmetica1 = Aritmetica(7, 9) #Les pasamos los argumentos para los operandos
print(f'La suma de los numeros es: {aritmetica1.sumar()}')
print(f'La resta de los numeros es: {aritmetica1.resta()}')
print(f'La multiplicación de los numeros es: {aritmetica1.multiplicar()}')
print(f'La división de los numeros es: {aritmetica1.dividir():.2f}') #muestra dsolo 2 numeros flotantes