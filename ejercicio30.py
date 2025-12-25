#Consigna: Verificar si una palabra es un palíndromo.

def darVueltaPalabra ():
    palabra = input('Indiqueme una palabra: ')

    palabraAlReves = palabra[::-1]
    if palabra == palabraAlReves:
        print('La palabra es un palíndromo')
    else:
        print('La palabra no es un palíndromo')


darVueltaPalabra()