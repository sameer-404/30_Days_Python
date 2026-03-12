#Write a lambda function which can solve a slope or y-intercept of linear functions.

# slope = (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# y-intercept: b = y - mx
y_intercept = lambda x, y, m: y - (m * x)

# Usage
m = slope(0, 0, 2, 4)
b = y_intercept(2, 4, m)

print(f"Slope: {m}")        # Slope: 2.0
print(f"Y-intercept: {b}")  # Y-intercept: 0.0