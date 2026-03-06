#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter your season: ")
month = month.lower()

summer = ["june", "july", "august"]
winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
autumn = ["september", "october", "november"]

if month in summer:
  print("Its summer!")
elif month in winter:
  print("Its winter!")
elif month in spring:
  print("Its spring!")
else:
  print("Its autumn")
