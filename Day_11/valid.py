#Write a function which check if provided variable is a valid python variable

def valid_keyword(keyword):
    if keyword[0].isdigit():
        print("Its invalid!")
        return
    
    for i in keyword:
        if not i.isalnum() and i != "_":
            print("Its invalid!")
            return
    
    print("Its valid!")

valid_keyword("_22")
valid_keyword("2hello")
valid_keyword("hello world")
valid_keyword("hello")