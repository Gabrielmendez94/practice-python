#Consigna: Pedir números hasta que el usuario ingrese 0.

def pedirNumeros():
    var = 1
    while (var != 0):
        var = int(input('Ingrese un numero: '))
    print('Listo')
    
pedirNumeros()