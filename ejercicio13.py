#Consigna: Pedir un número y mostrar si es par o impar.

def paridadNum():
    var1 = int(input('Indiqueme un numero, por favor: '))
    if((var1 %2) == 0):
        print('El numero ingresado es par')
    else:
        print('El numero ingresado es impar')

paridadNum()