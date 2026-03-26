#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

mixed = [1, 'Albania', True, 'Ethiopia', 3.14, 'Kenya', 42, 'Japan', 
         'Canada', False, 7, 'Nigeria', 2.5, 'Brazil', 99, 'India']

def get_string_lists(each):
  if type(each) == str:
    return True
  else:
    return False
  
string_list = list(filter(get_string_lists, mixed))
print(string_list)