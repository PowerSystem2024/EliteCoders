from abc import ABC,abstractmethod
#ABC SIGNIFICA:Clase base abstracta, convierte la clase en abstracta


class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        # Validar y asignar el valor del alto
        if self.validarValores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erróneo para el alto: {alto}")
        
        # Validar y asignar el valor del ancho
        if self.validarValores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erróneo para el ancho: {ancho}")

    def validarValores(self, valor):
        # Método de validación de valores (debe ser mayor que 0)
        return valor > 0

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        # Validación en el setter
        if self.validarValores(alto):
            self._alto = alto
        else:
            print(f"Valor no válido para el alto: {alto}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        # Validación en el setter
        if self.validarValores(ancho):
            self._ancho = ancho
        else:
            print(f"Valor no válido para el ancho: {ancho}")
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    def __str__(self):
        return f'Figura geométrica [Alto: {self.alto}, Ancho: {self.ancho}]'

    def validarValores(self, valor): #Metodo encapsulado
        return True if 0 < valor < 10 else False
    

    
    