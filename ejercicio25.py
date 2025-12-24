def factorial():
    num = int(input("Indiqueme de cual numero quiere conocer su factorial: "))
    valor = 1
    i = 1
    while (i < num):
        i +=1
        valor = valor * i
    print(f'El factorial de {num} es {valor}!')

factorial()