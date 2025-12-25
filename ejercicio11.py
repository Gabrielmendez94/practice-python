#Consigna: Calcular el area de un círculo.

import math
def calcAreaCirculo():
    print(f'Bienvenido al calculador de areas de circulos')
    var1 = int(input("Indiqueme la longitud en metros del radio de su circulo: "))
    print(f'El area de su rectangulo es de {math.pi * (var1 ** 2)} metros cuadrados.')


calcAreaCirculo()