import math

def area(radius):
  area = math.pi * radius * radius
  return area

r = int(input("What's the radius: "))
result = area(r)
print(f"The area of circle with radius-{r} is {result:.2f}")