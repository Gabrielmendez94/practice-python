def mayorDeEdad():
    edad = int(input('Indique cual es su edad: '))
    if (edad >= 18):
        print("Usted es mayor de edad y puede acceder")
    else:
        print("Lo siento, no tiene la edad suficiente para acceder.")


mayorDeEdad()