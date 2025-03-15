from datetime import datetime

date_string = "03/03/2025"

date_obj = datetime.strptime(date_string, "%d/%m/%Y")
print(date_obj)