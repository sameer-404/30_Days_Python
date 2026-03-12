#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
#generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
import random

def generate_colors(num):
  full_rgb = []
  
  for each in range(num):
    rgb = []
    for i in range(3):
      rgb.append(random.randint(0,250))
    full_rgb.append(f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")

  return full_rgb
  

num = int(input("Enter how many times you want the rgb: "))
result = generate_colors(num)

print(result)