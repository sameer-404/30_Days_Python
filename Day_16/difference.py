#Calculate the time difference between now and new year.

from datetime import datetime

new_year = datetime(2026, 1, 1)
new_year = new_year.date()
print(new_year)

now = datetime.now()
current_date = now.date()
print(current_date)

difference = current_date - new_year
print(difference.days)