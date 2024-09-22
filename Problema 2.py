consumo = float(input("Introduce el monto de tu consumo en el restaurante: "))
porcentaje = float(input("Introduce el porcentaje de propina que deseas dejar: "))
propina = consumo * (porcentaje/ 100)

print(f"La cantidad de propina es: {propina}")