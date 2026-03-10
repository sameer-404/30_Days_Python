#Create a function called show_args to take an arbitrary number of named arguments and print their names and values.

def show_args(**args):
  for k,v in args.items():
    print(f"key: {k} , value: {v}")

show_args(name = "sameer", age = 21, school = "GSU") 