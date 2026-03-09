#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    all_valid = True  # flag to track if all inputs are valid
    
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            print("Please provide all number types as arguments!")
            all_valid = False
    
    if all_valid:
        return total
    else:
        return None

result = add_all_nums(2, 3, 4, 5)
if result is not None:
    print(f"The total sum is: {result}")
