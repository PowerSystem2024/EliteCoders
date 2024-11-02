from Orden import Orden
from Producto import Producto

producto1 = Producto('Remera', 100.00)
producto2 = Producto('Camisa', 200.00)
producto3 = Producto('Cinto', 200.00)
producto4 = Producto('Zapatos', 400.00)
producto5 = Producto('Corbata', 500.00)
producto6 = Producto('Hoodie', 4000.00)

productos1 = [producto1, producto2]  # Lista de productos
orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos

orden1.agregar_producto(producto5)
orden1.agregar_producto(producto3)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')

# Orden 2
productos2 = [producto3, producto4]
orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto5)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')