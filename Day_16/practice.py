#Python Date Time:


#bro code:

"""import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

print(date)
print(today)
print(time)

now = now.strftime("%H:%M:%S %m %d %Y")

print(now)


target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
  print("Target Date has passed!")
else:
  print("Target date has now passed! ")"""

#Getting Datetime information:

"""from datetime import datetime

now = datetime.now()
print(now) 

day = now.day
print(day)
month = now.month
minute = now.minute
print(month, minute)
"""
"""timestamp = now.timestamp()
print(timestamp)""" #not so important


#formatting date output using surftime:
"""from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M:%S")
print(f"Time {t}")

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)"""


#String to time using strptime:

"""from datetime import datetime

date_string = "5 december, 2019"
print(date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y" )
print(date_object.date())"""


#Using Date from Datetime:
"""
from datetime import date
d = date(2020, 1, 1)
print(d)

print(f"Current Date: {d.today()}")

#date object of today's date:
today = date.today()
print("Current year: ", today.year)"""