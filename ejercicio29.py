#Consigna: Pedir una palabra y mostrarla al revés.

def mostrarPalabraALReves():
    palabra = input('Indiqueme cual es su palabra: ')
    i = len(palabra) - 1
    while (i >= 0):
        print(palabra[i], end="")
        i-=1

mostrarPalabraALReves()