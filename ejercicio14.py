def compNum():
    var1 = int(input('Ingrese el primer numero, por favor: '))
    var2 = int(input('Ingrese el segundo numero, por favor: '))
    var3 = int(input('Ingrese el tercer numero, por favor: '))

    if(var1 > var2):
        if(var1 > var3):
            input(f'El numero mayor de los 3 es el {var1}')
        else:
            input(f'El numero mayor de los 3 es el {var3}')
    elif(var1 < var2):
        if(var2 > var3):
            input(f'El numero mayor de los 3 es el {var2}')
        else:
            input(f'El numero mayor de los 3 es el {var3}')


compNum()