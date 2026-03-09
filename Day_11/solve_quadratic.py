import math

def solve_quadratic(a, b, c):
    dis = (b*b) - 4*a*c

    if dis > 0:
        print("There will be two solutions!")
        x1 = (-b + math.sqrt(dis)) / (2*a)
        x2 = (-b - math.sqrt(dis)) / (2*a)
        return x1, x2

    elif dis < 0:
        return "No solution"

    else:
        print("There will be one solution!")
        x = -b / (2*a)
        return x

print("Please provide your values for Ax^2 + Bx + C = 0 in the same format!")
print("If you dont have a value for any of them type: 0")
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

result = solve_quadratic(a, b, c)

if result == "No solution":
    print("There was no real solution!")
elif isinstance(result, tuple):  # ✅ two solutions
    print(f"The solutions are: {result[0]} and {result[1]}")
else:                             # ✅ one solution (float)
    print(f"The solution is: {result}")