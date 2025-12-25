#Consigna: Contar cuántos números ingresó el usuario antes de ingresar 0.

def pedirNumeros():
    contador = 0
    var = 1
    while (var != 0):
        var = int(input('Ingrese un numero: '))
        contador += 1
    print('Listo')
    print(f'El usuario ingresó {contador - 1} números antes de ingresar 0')
    
pedirNumeros()