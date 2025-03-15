from datetime import datetime

now = datetime.now()
dayweek = now.weekday()

if dayweek == 0:
    print("Hoy es lunes")
elif dayweek == 1:
    print("Hoy es martes")
elif dayweek == 2:
    print("Hoy es miercoles")
elif dayweek == 3:
    print("Hoy es jueves")
elif dayweek == 4:
    print("Hoy es viernes")
elif dayweek == 5:
    print("Hoy es sabado")
elif dayweek == 6:
    print("Hoy es domingo")