#Write a function called is_prime, which checks if a number is prime.

def is_prime(num):
  my_set = set()
  for i in range(2,num,1):
    if num % i == 0:
      my_set.add(i)
    else:
      pass

  if len(my_set) != 0:
    print("Its not a prime number!")
  else:
    print("Its a prime number!")

your_num = int(input("Enter your number: "))
is_prime(your_num)