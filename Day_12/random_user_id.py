#Write a function which generates a six digit/character random_user_id.

import random
import string

def random_user_id():
    my_chars = string.ascii_lowercase + string.digits
    result = ""
    
    for i in range(6):
        result += random.choice(my_chars)
    
    return result

print(random_user_id())