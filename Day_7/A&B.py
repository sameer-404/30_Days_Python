A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Join A and B
joined = A.union(B)
print(joined)

#Find A intersection B
intersection = A.intersection(B)
print(intersection)

#Is A subset of B
result = A.issubset(B)
print(result)

#Are A and B disjoint sets
result2 = A.isdisjoint(B)
print(result2)