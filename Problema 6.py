# Solicita al usuario que introduzca la edad del cliente
edad = int(input("Introduce la edad del cliente: "))
# Determina el precio de la entrada según la edad
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

print(f"El precio de la entrada es: {precio}")

