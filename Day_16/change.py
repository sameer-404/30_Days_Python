#Today is 5 December, 2019. Change this time string to time.

from datetime import datetime

current_date = "5 December, 2019"
current_date_numerical = datetime.strptime(current_date, "%d %B, %Y")
print(current_date_numerical.date())