#Ejercicio 4: Calculadora de Impuestos
#Crear una funcion para calcular el total de un pago iclutyendo
#un impuesto aplicado (IVA)
#Formula: pago_total = pago_sin_impuesto + (pago_sin_impuesto * (impuesto/100))
#Poroporcione el pago sin impuesto: 1000
#Proporcione el monto del impuesto: 21%
#Pago con impuesto: xxxx

def calcular_impuestos(pago_sin_impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (21/100)
    print('El pago sin impuestos es: ', pago_sin_impuesto)
    print('El impuesto es: 21%')
    print("El pago con impuestos es: ", pago_total)

calcular_impuestos(int(input("Proporcione el importe a pagar: ")))