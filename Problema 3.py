peso_payaso = 112
peso_muneca = 75
numero_payasos = int(input("Introduce el número de payasos: "))
numero_munecas = int(input("Introduce el número de muñecas: "))
#hallar el peso total
peso_total = (numero_payasos * peso_payaso) + (numero_munecas * peso_muneca)
print(f"El peso total del paquete es: {peso_total} gramos")