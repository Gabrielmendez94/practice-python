#Consigna: Mostrar los números del 10 al 1 usando while.

numeros = [1,3,6,7,5,4,9,8,10,2]
i = 0

while (i < len(numeros) - 1):
    if(numeros[i] < numeros[i+1]):
        numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
        i+=1

print(numeros)