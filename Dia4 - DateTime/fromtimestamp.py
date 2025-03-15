from datetime import datetime

# Obtener la marca de tiempo actual (segundos desde 1970-01-01)
marca_de_tiempo = 1677657600  # Esta es una marca de tiempo de ejemplo

# Convertir la marca de tiempo a un objeto datetime
fecha_hora = datetime.fromtimestamp(marca_de_tiempo)

print(fecha_hora)  # Muestra la fecha y hora correspondiente a la marca de tiempo