#Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime

now = datetime.now()
day = now.day
print(day)
month = now.month
print(month)
year = now.year
print(year)
hour = now.hour
print(hour)
minute = now.minute
print(minute)
timestamp = now.timestamp()
print(timestamp)