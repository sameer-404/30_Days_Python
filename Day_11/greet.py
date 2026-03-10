#Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

def greet(name="Guest"):
    print(f"Hello, {name}!")

Name = input("Enter your name: ")
greet(name=Name if Name else "Guest")