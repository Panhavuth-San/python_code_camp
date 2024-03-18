#4. Create a function that receives and array(list) and search element(number to be found from the array).
#The function must return the position of the search number in the array if the search number is not available in the array
#then return "Element not found in the array!".
user_list = input("input an array/list here: ")
user_search = int(input ("Enter number to find: "))
lists = user_list.split()

#convert list of string to list of int
for i in range(0, len(lists)):
    lists[i] = int(lists[i])

#function for searching
def  search_element (array,num):
    location =-1
    value=-1
    for i in range (0,len(array)):
        if  num == array [i]:
            location = i
            value= array[i]
    if (location != -1):
        print("Element ",value,"found at index", location)
    else :
        print("Element not found in the array")
search_element(lists,user_search)
