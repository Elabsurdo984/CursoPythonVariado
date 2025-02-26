import random

# Lista de elementos
lista_elementos = ["manzana", "silla", "mesa", "microfono"]

# Pesos que determinan la probabilidad de seleccion (la manzana tiene mas posibilidades)
pesos = [0.1, 0.3, 0.6, 0.9]

# Selecciona 5 elementos aleatorios con remplazo segun los pesos
resultados = random.choices(lista_elementos, weights=pesos, k=1)
print(resultados)