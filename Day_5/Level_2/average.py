#Find the average age (sum of all items divided by their number )
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

total = 0
for age in ages:
    total += age

n = len(ages)
average = total/n
print(f"Average: {average}")
