#Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]
range_of_ages = max_age - min_age
print(range_of_ages)