#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
  factorial = 1
  for i in range(1,num+1, 1):
    factorial = factorial * i
  return factorial

fact = factorial(5)
print(fact)