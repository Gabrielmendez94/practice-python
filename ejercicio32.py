#Consigna: Reemplazar todas las vocales de una palabra por *.

vocales = ['a','e','i','o','u']

def reemplazarVocal():
    palabra=input('Indiqueme una palabra, por favor: ')
    nueva_palabra = ""
    for letra in palabra:
        if letra.lower() in vocales:
            nueva_palabra += "*"
        else:
            nueva_palabra += letra

    print(nueva_palabra)

reemplazarVocal()