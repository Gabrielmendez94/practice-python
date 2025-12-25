#Consigna: Sumar todos los números ingresados hasta que se ingrese 0.

def pedirNumeros():
    contador = 0
    var = 1
    while (var != 0):
        var = int(input('Ingrese un numero: '))
        contador = contador + var
    print('Listo')
    print(f'El valor de la suma de los numeros ingresados antes del 0 es {contador}')
    
pedirNumeros()