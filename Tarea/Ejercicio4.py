def comprobarFormato(telefono):

    while True:

        if len(telefono) == 16 and telefono[3] == '-' and telefono[13] == '-' and telefono[0] == '+' and telefono.replace("+","").replace("-","").isdigit():
            print("número ingresado correctamente...\n")
            return telefono
        else:
            print("Formato incorreecto.\n")
            telefono = str(input("Introduzca un número de teléfono con el siguiente formato:\n"
                                 "Prefijo-Número-Extensión\n"   
                                 "+34-913724710-56\n\n"))

numeroDeTelefono = str(input("Introduzca un número de teléfono con el siguiente formato:\n"
                             "Prefijo-Número-Extensión\n"
                             "+34-913724710-56\n\n"))

numeroDeTelefono = comprobarFormato(numeroDeTelefono)

soloNumero = numeroDeTelefono[4:13]
print("El número de teléfono sin prefijo ni extensión es:")
print(soloNumero) 

