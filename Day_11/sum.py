def add_two_numbers(num1, num2):
  sum = num1 + num2
  return sum

first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
result = add_two_numbers(first, second)
print(f"The sum is {result}")