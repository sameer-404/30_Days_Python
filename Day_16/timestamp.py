#Calculate the time difference between 1 January 1970 and now.

from datetime import datetime

now = datetime.now()
timestamp = now.timestamp()
print(f"Time Difference in seconds: {timestamp:.2f}")
days = timestamp/86400
print(f"Time Difference in days: {days:.2f}") 