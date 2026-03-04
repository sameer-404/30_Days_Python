#Slice out the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon", "Anthropic"]
length = len(it_companies)

#checking if its even or odd:
if length % 2 == 1:
  print("Its odd")
  middle_index = length//2
  print(f"Middle company is {it_companies[middle_index]}")
else:
  print("Its Even")
  middle_index1 = (length//2)-1 
  middle_index2 = (length//2)
  print(f"Middle companies are: {it_companies[middle_index1]} and {it_companies[middle_index2]}")
