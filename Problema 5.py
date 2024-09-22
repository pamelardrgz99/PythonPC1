numero_shows = int(input("¿Cuántos shows musicales has visto en el último año?: "))

# Determina si el usuario ha visto más de 3 shows
vista_mas_de_tres_shows = numero_shows > 3

# Muestra el resultado en pantalla
print(f"¿Has visto más de 3 shows musicales?: {vista_mas_de_tres_shows}")