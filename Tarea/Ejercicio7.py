correo = input("Escribe un correo electrónico:\n")

primeraParte = correo.split("@")[0]

print(primeraParte + str("@ceu.es"))