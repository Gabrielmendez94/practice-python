def evaluadorDeNotas():
    nota = int(input('Indiqueme cual es su nota: '))
    if(nota >= 8 | nota <=10):
        print('Usted promocionó la materia. No es necesario que rinda final')
    elif(nota > 10):
        print('Error, la nota que usted indicó no es correcta.')
    elif(nota >=6 | nota <8):
        print('Usted aprobó la materia, pero no la promocionó. Va a tener que rendir final')
    else:
        print('Usted desaprobó la materia.')

evaluadorDeNotas()