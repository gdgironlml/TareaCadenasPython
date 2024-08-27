def comprobarVocal(v):
    caracteresPermitidos = 'aeiou'

    while True:

        if v in caracteresPermitidos:
            print("Carácter correcto\n")
            return v
        else:
            print("Carácter incorrecto")
            v = input("Introduzca una vocal:\n")

frase = input("Introduzca una frase:\n")
vocal = input("introduzca una vocal:\n")

vocal = comprobarVocal(vocal)
vocalMayuscula = vocal.upper()

fraseModificada = frase.replace(vocal,vocalMayuscula)

print(fraseModificada)