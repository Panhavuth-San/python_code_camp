#Write a function that receives an argument and generate random number between 0 to 100 for n times based on the argument and stored in a tuple. Display the tuple and return the sum of numbers to the caller.
import random
user_input = input("Enter numbers of generation: ")
tuples = ()
def random_tuple (user_input,tuples):
    for i in range(int(user_input)):
        rand_num = random.randint(0,100)
        tuples += (rand_num,)
        print("Random number",i+1,": ",rand_num)
    print(tuples)
    print(sum(tuples))
random_tuple(user_input,tuples)