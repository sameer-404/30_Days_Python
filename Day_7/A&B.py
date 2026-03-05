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

#Join A with B and B with A
A_join_B = A.union(B)
B_join_A = B.union(A)
print(A_join_B)
print(B_join_A)

#What is the symmetric difference between A and B
diff = A.symmetric_difference(B)
print(diff)

#Delete the sets completely 
del A
del B
#print(A) will raise an error
#print(B) will raise an error 
