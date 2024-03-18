#Write a python function that receives a tuple and search number in the arguments and return the index of the search number from the tuple. If the search number is not found in the tuple return “Element not found in the tuple”.
def search_in_tuple(tuple,search):

        if search in tuple:
            print ("Element found at index",tuple.index(search))
        else:
            print("Element not found in the tuple")
            
search_in_tuple((20,15,10,30),10)
search_in_tuple((20,15,10,30),40)

