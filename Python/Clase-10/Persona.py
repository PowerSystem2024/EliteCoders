class Persona:
    #variables de clase
    contador_personas=0 
    
    #Metodo de clase
    @classmethod
    #cremos un metodo
    def generar_siguiente_valor(cls):
        #vamos incrementando
        cls.contador_personas += 1 
        return cls.contador_personas
    
    
    #creo un metodo y inicializo el contructor con las variables
    def __init__(self,nombre, edad):
        self.id_persona= Persona.generar_siguiente_valor()
        self.nombre= nombre
        self.edad=edad
    
    #creo otro metodo para retornar la persona con sus atributos
    def __str__(self):
        return f'Persona[{self.id_persona} = {self.nombre} {self.edad}]'

#Defino los valores de cada persona y imprimo
persona1=Persona("Matias", 18)
print(persona1)
persona2=Persona("Franco", 25)
print(persona2)
persona3=Persona("Marina", 25)
print(persona3)
Persona.generar_siguiente_valor()
persona4=Persona("Mariana",35)
print(persona4)

#Imprimos el contador persona
print(f"Valor contador personas:{Persona.contador_personas} ")
