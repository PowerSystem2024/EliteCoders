#Ejercicio 4: Calculadora de inpuestos
#crear una funcion para calcular el total de un pagp incluyendo
#un impuesto aplicado(iva)
#formula: pagototal=pagosinimpuesto + pagosinimpuesto * (impuesto/100)
#Proporcone el pago sin impuesto:1000
#proporcione elmonto del impuesto:21%
#Pago con impuesto: xxxxxx

#Pedimos al usuario que digite el monto y el impuesto
monto=int(input("Digite el monto : "))
impuesto=int(input("Digite el impuesto: "))
#Creamos una funcion y calculamos el moto total
def pago(monto):
    montoTotal= monto + monto * (impuesto/100)
    #Imprimimos y retornamos
    print(montoTotal)
    return montoTotal
#llamamos a la funcion
pago(monto)
