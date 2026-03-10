#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
"""
# rgb(125,244,255) - the output should be in this form
"""
import random

def rgb_color_gen():
    r = str(random.randint(0, 255)).zfill(3)
    g = str(random.randint(0, 255)).zfill(3)
    b = str(random.randint(0, 255)).zfill(3)
    print(f"rgb({r},{g},{b})")

rgb_color_gen()