# Importamos el módulo math para poder usar funciones matemáticas como pi y e
import math

# Definimos el valor del radio del círculo
radio = 5

# Calculamos el área del círculo usando la fórmula: Área = pi * radio^2
# math.pi es una constante que tiene el valor de pi (aproximadamente 3.14159)
area_circulo = math.pi * radio ** 2

# Calculamos la circunferencia del círculo usando la fórmula: Circunferencia = 2 * pi * radio
circunferencia = 2 * math.pi * radio

# Definimos el exponente para la operación con 'e'
exponente = 2

# Calculamos el valor de e elevado a un exponente utilizando la constante math.e
# math.e es una constante que tiene el valor de e (aproximadamente 2.71828)
resultado_exponencial = math.e ** exponente

# Imprimimos el área del círculo con solo 2 decimales
# La notación {:.2f} significa que mostramos el número con 2 decimales después del punto
print(f"Área del círculo con radio {radio}: {area_circulo:.2f}")

# Imprimimos la circunferencia del círculo con solo 2 decimales
# De nuevo, usamos la notación {:.2f} para limitar los decimales a 2
print(f"Circunferencia del círculo con radio {radio}: {circunferencia:.2f}")

# Imprimimos el resultado de e elevado a 2, también con 2 decimales
print(f"Resultado de e elevado a {exponente}: {resultado_exponencial:.2f}")
