# Prueba:
try:
    # Variable resultado que almacena 10 dividido 0 (Error)
    resultado = 10 / 0

# Si da error de division por cero:
except ZeroDivisionError:
    # Imprimir "Error: No se puede dividir por cero"
    print("Error: No se puede dividir por cero")

# En caso de que no suceda el error:
else:
    # Imprimir "La operacion fue exitosa: {resultado}". 
    # La variable "Resultado es el resultado de la division si algo sale bien
    print(f"La operacion fue exitosa: {resultado}")

# Finalmente:
# Este codigo se ejecuta PASE LO QUE PASE
finally:
    print("Esto se ejecuta")