contraseña = "Leonardo_94"

def validarIdentidad():
    password = input('Escriba su contraseña: ')
    if(contraseña == password):
        print('Acceso correcto')
    else:
        print('Acceso incorrecto. Vuelva a intentarlo')


validarIdentidad()