#Consigna: Convertir grados Celsius a Fahrenheit.

def conversorCelciusAFahrenheit ():
    var = int(input("Ingrese los grados celcius que desea convertir a Fahrenheit: "))
    conversor = (var * (9/5)) + 32
    print(f'La equivalencia de {var} grados celcius a grados fahrenheit es: {conversor} grados fahrenheit')


conversorCelciusAFahrenheit()