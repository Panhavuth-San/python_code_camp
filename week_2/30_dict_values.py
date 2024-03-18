#Write a python function that receives a dictionary with integer and Tuples of strings as values. The function must iterate and display all the values present in each tuple along with its key. Every time the function prints a set tuple values it must separate the values with a new line and also ****
dictionary1= {
    120: ("visal","Borey", "Sovann"),
    130: ("Hout","Mouyleng","Pidor"),
} 
def dict(dictionary1):
    for key, value in dictionary1.items():
        
        print(key," : ", end=" ")
        for i in value:
            print(i, end=" ",)
        print("\n*****")
dict(dictionary1)
