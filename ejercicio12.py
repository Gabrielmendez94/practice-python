def tipoNumero (num):
    var1 = int(input('Ingrese un numero, por favor: '))
    if(var1 > 0):
        print("Su numero es positivo")
    elif(var1 < 0):
        print('Su numero es negativo')
    else:
        print('Su numero es 0')

tipoNumero(5)