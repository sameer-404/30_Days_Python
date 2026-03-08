#Use for loop to iterate from 0 to 100 and print only even numbers

"""for word in range(0,101,2):
  print(word)"""

#Rather use this:
for i in range(101):
    if i % 2 == 0:
        print(i) 