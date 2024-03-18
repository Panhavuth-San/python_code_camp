#3. Create a function that accepts name as the argument and prints the middle character of the name
user_input = input("input name: ")
def print_middle(name):
    print(name[len(name)//2])
print_middle(user_input)