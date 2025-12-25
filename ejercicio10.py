#Consigna: Calcular el área de un rectángulo.

def calcAreaRectangulo():
    print(f'Bienvenido al calculador de areas de rectangulos')
    var1 = int(input("Indiqueme la longitud en metros del lado 1 de su rectangulo: "))
    var2 = int(input("Indiqueme la longitud en metros del lado 2 de su rectangulo: "))
    print(f'El area de su rectangulo es de {var1 * var2} metros cuadrados.')


calcAreaRectangulo()