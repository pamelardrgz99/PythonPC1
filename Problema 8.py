# Introducir la hora
time = input("Introduce la hora en formato hh:mm : ")

# Divide la entrada en horas y minutos
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

# Convierte la hora a un valor float
hora_del_dia = hours + (minutes / 60)

# Mostrar resultados
if 7 <= hora_del_dia <= 8:
    print("Es la hora del desayuno.")
elif 12 <= hora_del_dia <= 13:
    print("Es la hora del almuerzo.")
elif 18 <= hora_del_dia <= 19:
    print("Es la hora de la cena.")