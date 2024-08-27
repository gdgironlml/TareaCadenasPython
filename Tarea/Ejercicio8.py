precio = input("Introduzca el precio del producto:\n")

if "." in precio:
    euros = precio.split(".")[0]
    centimos = precio.split(".")[1]
else:
    euros = precio
    centimos = "00"

print("El precio es de:")
print(str(euros + " euros"))
print(str(centimos + " céntimos"))