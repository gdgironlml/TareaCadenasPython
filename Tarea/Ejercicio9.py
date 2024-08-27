from datetime import datetime

fechaNacimiento = input("Escriba su fecha de nacimiento en el siguiente formato:\n"
                        "dd/mm/aaaa\n")

fechaCorregida = datetime.strptime(fechaNacimiento, "%d/%m/%Y")

print(str("Día ") + fechaCorregida.strftime("%d"))
print(str("Mes ") + fechaCorregida.strftime("%m"))
print(str("Año ") + fechaCorregida.strftime("%Y"))