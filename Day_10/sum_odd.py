#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

total1 = 0
total2 = 0
for i in range(101):
  if i % 2 == 1:
    total1 += i
  else:
    total2 += i

print(f"The sum of odd is {total1} and even is {total2} ")