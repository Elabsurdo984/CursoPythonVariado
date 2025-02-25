import math

# Parametros del pendulo:
g = 9.81   # aceleración debido a la gravedad (m/s^2), constante en la superficie de la Tierra
L = 1.0    # longitud del péndulo (en metros), podemos cambiarlo para simular un péndulo más largo o corto
theta_0 = math.radians(30)  # ángulo inicial del péndulo en grados (30°), lo convertimos a radianes con math.radians

# Tiempo de simulacion:
# Generamos una lista de tiempos desde 0 hasta 10 segundos, con intervalos de 5 segundos
tiempo = [t * 0.5 for t in range(21)]  # Usamos el rango de 0 a 10 segundos, con pasos de 0.5 segundos

# Imprimimos un encabezado para la salida en consola, indicando las unidades de tiempo y angulo
print("Tiempo (segundos) | Angulo (radianes)")
print("------------------|------------------")

# Empezamos un bucle que recorrera todos los tiempos generados
for t in tiempo:
    # Calculamos el angulo en funcion del timepo usando la formula:
    # θ(t) = θ₀ * cos(√(g / L) * t)
    # Esto nos da el ángulo en radianes para cada valor de t
    angulo = theta_0 * math.cos(math.sqrt(g / L) * t)

    # Imprimimos el tiempo (t) y el angulo calculado (angulo) con un formato especifico:
    # t con 1 decimal, angulo con 4 decimales para mayor precision
    print(f"{t:18.1f} | {angulo:18.4f}")