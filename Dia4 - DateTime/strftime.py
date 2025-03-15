from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%d/%m/%y")

print(formatted_date)