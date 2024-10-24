class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = "Esta es una variable de clase"

    def __init__(self, variable_intancia):
        # La variable de instancia da diferentes valores a cada objeto
        self.variable_intancia = variable_intancia

    @staticmethod
    def metodo_estatico():#Metodo estatico se asocia a la clase
        print(MiClase.variable_clase)
    @classmethod
    def metodo_clase(cls): #EL cls es una referencia a la clase en si misma
        print(cls.metodo_clase)
    
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_intancia)
# Acceso a la variable de clase desde la clase directamente
print(MiClase.variable_clase)

# Creación de la primera instancia de la clase
miClase1 = MiClase("Esta es una variable de instancia")
# Acceso a la variable de instancia desde la primera instancia
print(miClase1.variable_intancia)
# Acceso a la variable de clase desde la primera instancia
print(miClase1.variable_clase)

# Creación de la segunda instancia de la clase
miClase2 = MiClase("Esta es otra prueba de una variable de instancia")
# Acceso a la variable de instancia desde la segunda instancia
print(miClase2.variable_intancia)
# Acceso a la variable de clase desde la segunda instancia
print(miClase2.variable_clase)


MiClase.variable_clase2= "Valor de variable de clase 2"

print(MiClase.variable_clase2)

print(miClase1.variable_clase2)

print(miClase2.variable_clase2)

MiClase.metodo_estatico()

MiClase.metodo_clase()
#creamos un objeto
miObjeto1=MiClase("Variable de instancia")
miClase1.metodo_clase()
miClase1.metodo_instancia()
