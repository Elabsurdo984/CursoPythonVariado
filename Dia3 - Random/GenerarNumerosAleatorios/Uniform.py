import random

# Dos numeros flotantes entre 10 y 100
flotante_aleatorio = random.uniform(10, 100)
otro_flotante_aleatorio = random.uniform(10, 100)

# Convierte a string los dos numeros
convertir = str(flotante_aleatorio)
convertir2 = str(otro_flotante_aleatorio)

# Concatenamos los dos numeros con un espacio entre medio (opcional)
print(convertir + " " + convertir2)