#Consigna: Contar cuántas vocales tiene una palabra.

vocales = ['a','e','i','o','u']

def contadorVocales():
    palabra=input('Indiqueme una palabra, por favor: ')
    contador=0
    for letra in palabra:
        if letra.lower() in vocales:
            contador+=1

    print(f'La palabra tiene {contador} vocales')

contadorVocales()