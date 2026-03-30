#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime

now = datetime.now()
result = now.strftime("%m/%d/%Y, %H:%M:%S")
print(result)