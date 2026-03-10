#Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(text):
  if len(text) == 0:
    return "Empty"
  else:
    return "It's not empty"

text = input("Enter your text: ")
result = is_empty(text)
print(result)