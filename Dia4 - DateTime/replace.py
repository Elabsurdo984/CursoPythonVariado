from datetime import datetime

now = datetime.now()

new_date = now.replace(year=2025, month=12, day=25, hour=10, minute=12, second=50, microsecond=31416)
print(new_date)
