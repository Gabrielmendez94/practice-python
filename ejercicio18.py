#Consigna: Mostrar la tabla de multiplicar de un número ingresado.

def tablaDeMultiplicar():
    numeroAMultiplicar = int(input('Indiqueme el numero del cual quiere conocer su tabla: '))
    i = 1
    tabla=[]
    while(i <= 10):
        tabla = numeroAMultiplicar  * i
        print(tabla)
        i+=1


tablaDeMultiplicar()