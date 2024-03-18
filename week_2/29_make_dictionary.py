#Write a python function that receives a list of integers and a tuple of strings in the arguments. The function must return a dictionary which is formed with the list element as keys and tuple elements as the values.
# convert user input into list
list_input = input("Enter key here: ")
lists=[]
lists = list_input.split()
#convert list value from str to int
for i in range(len(lists)):
    lists[i] = int(lists[i])

#convert user input into tuple
tuple_input = tuple(input("Enter Key value here: ").split(" "))

dictionary_list = {}
def make_dictionary (list_input,tuple_input):
    for i in range(len(list_input)):
            dictionary_list[list_input[i]] = tuple_input[i]
    return dictionary_list
print(make_dictionary(lists,tuple_input))


