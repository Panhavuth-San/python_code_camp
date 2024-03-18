#You will write a function that take 3 parameters, combine them and return the parameters as a List. However, you function must support any number of arguments
def make_list(*args):
    return list(args)
print(make_list(21,"Hello",45))