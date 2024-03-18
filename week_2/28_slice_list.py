#Write a python function that receives a list and a slice_number in the arguments. The function must return a new list which is retrieved after slicing the list from front and rear with the slice_number. If the second argument is 2 then 2 numbers at the front and back must be removed in the returned list.
def slice_list(list,index):
    return list[index:-index]
# Testing the function with a sample input
list1=[1,2,3,4,5,6,7]
print(slice_list(list1, 2))