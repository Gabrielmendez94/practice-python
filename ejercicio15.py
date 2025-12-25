#Consigna: Mostrar los números del 1 al 10 usando for.

numeros= [4,3,6,1,5,8,2,9,7,10]

for i in range(len(numeros)):
    for j in range(len(numeros)-1):
        if(numeros[j] > numeros[j+1]):
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print(numeros)


otrosNumeros = [3,5,7,8,1,2,4,6,9,10]
otrosNumeros.sort()
print(otrosNumeros)