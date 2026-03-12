#Write a function generate_colors which can generate any number of hexa or rgb colors.

import random

def generate_colors(color_type, number):
    colors = []

    if color_type == "hexa":
        options = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for each in range(number):
            color_code = ""
            for i in range(6):
                color_code += random.choice(options)
            colors.append("#" + color_code)

    elif color_type == "rgb":
        for each in range(number):
            rgb = []
            for i in range(3):
                rgb.append(random.randint(0, 255))
            colors.append(f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")

    return colors

print(generate_colors("hexa", 3))
print(generate_colors("rgb", 3))