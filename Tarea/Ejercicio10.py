productosSeleccionados = input("Ingrese dos de los siguientes productos separados por una coma ',':\n"
                                "1 - Guitarra\n"
                                "2 - Bajo\n"
                                "3 - Amplificador\n"
                                "4 - Cable\n"
                                "5 - Pedal de distorcion\n"
                                "6 - Pedal de delay\n"
                                "7 - Pedal de compresion\n"
                                "8 - Pedal de reverb\n")

ProductosEnLista = productosSeleccionados.split(",")

print("Has seleccionado:")
print(ProductosEnLista[0].strip())
print(ProductosEnLista[1].strip())