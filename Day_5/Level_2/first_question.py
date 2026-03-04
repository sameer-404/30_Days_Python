#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print(min_age)
print(max_age)

#Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

#Find the median age (one middle item or two middle items divided by two)
length_of_ages = len(ages)
print(length_of_ages)

if length_of_ages//2 == 1:
  print("Its odd!")
  median_age = ages[length_of_ages//2]
  print(median_age)
else:
  print("Its even!")
  median_age1 = ages[length_of_ages//2]
  median_age2 = ages[(length_of_ages//2)+1]
  print(f"median_ages are: {median_age1}, {median_age2}")
  if median_age1 == median_age2:
    print(f"Median age: {median_age1}")