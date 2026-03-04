#Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]
range_of_ages = max_age - min_age
print(range_of_ages)

total = 0
for age in ages:
    total += age

n = len(ages)
average = total/n
print(f"Average: {average}")

min_to_average = average - min_age
ave_to_max = max_age - average

print(f"The difference is : {min_to_average:.2f}") 
print(f"The difference is : {ave_to_max:.2f}") 

