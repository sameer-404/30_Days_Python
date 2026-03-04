#Remove the first IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies.pop(0)
print(it_companies)

length = len(it_companies)

#Remove the middle IT company or companies from the list
if length % 2 == 1:
  print("Its odd")
  middle_index = length//2
  it_companies.pop(middle_index)
  print(it_companies)
else:
  print("Its Even")
  middle_index1 = (length//2)-1 
  middle_index2 = (length//2)
  del it_companies[middle_index1:middle_index2+1]
  print(it_companies)

#Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies
#print(it_companies)