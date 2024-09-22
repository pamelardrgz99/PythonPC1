num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Muestra el menú de opciones
print("Elige una opción:")
print("1. Mostrar una suma de los dos números")
print("2. Mostrar una resta de los dos números (el primero menos el segundo)")
print("3. Mostrar una multiplicación de los dos números")

# Elegir una opcion
opcion = int(input("Introduce el número de la opción deseada: "))

#Mostrar resultados
if opcion == 1:
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == 2:
    resultado = num1 - num2
    print(f"La resta de {num1} menos {num2} es: {resultado}")
elif opcion == 3:
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
else:
    print("Opción no válida. Por favor, elige una opción correcta.")