#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random
import string

def user_id_gen_by_user():
    num_of_chars = int(input("Enter number of characters: "))
    num_of_ids = int(input("Enter number of IDs: "))
    
    my_chars = string.ascii_lowercase + string.digits
    
    for i in range(num_of_ids):
        result = ""
        for j in range(num_of_chars):
            result += random.choice(my_chars)
        print(result)

user_id_gen_by_user()