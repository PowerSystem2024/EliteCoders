from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '15 PULGADAS')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Samsung', 'USB')
monitor2 = Monitor('Samsung', '24 PULGADAS')
raton2 = Raton('Samsung', 'Bluetooth')
computadora2 = Computadora('Samsung', monitor2, teclado2, raton2)

teclado3 = Teclado('Dell', 'Bluetooth')
monitor3 = Monitor('Dell', '27 PULGADAS')
raton3 = Raton('Dell', 'Bluetooth')
computadora3 = Computadora('Dell', monitor3, teclado3, raton3)

teclado4 = Teclado('Acer', 'Bluetooth')
monitor4 = Monitor('Acer', '17 PULGADAS')
raton4 = Raton('Acer', 'USB')
computadora4 = Computadora('Acer', monitor4, teclado4, raton4)

teclado5 = Teclado('Gamer', 'Bluetooth')
monitor5 = Monitor('Gamer', '27 PULGADAS')
raton5 = Raton('Gamer', 'USB')
computadora5 = Computadora('Acer', monitor5, teclado5, raton5)

computadora6 = Computadora('Apple', monitor1, teclado3, raton4)
computadora7 = Computadora('LG', monitor5, teclado1, raton2)


compu1 = [computadora1, computadora2, computadora7, computadora4]
orden1 = Orden(compu1)
orden1.agregar_computadora(computadora3)
print(orden1)

compu2 = [computadora3, computadora5, computadora6]
orden2 = Orden(compu2)
orden2.agregar_computadora(computadora1)
print(orden2)
