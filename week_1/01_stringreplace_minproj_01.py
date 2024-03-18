#important var
yes_no=-1
options=["y",'n']
paragraph_list=[]
#user input
paragraph_input=input("Enter a paragraph:")
word_search = input("Enter word to search here: ")

#count of repeated occurences of the word
count = paragraph_input.count(word_search)
print("There are",count,"occurences")

while yes_no ==-1:
    ask_change=input("Do you want to replace the text [Y/N]? ").lower()
    if ask_change not in options:
        print("Please give proper input !")
        continue
    elif  ask_change == "n" or ask_change == "N":
        print("Oh! you don't like to replace")
        ask_change =input("Do you want check again [Y/N]? ").lower()
        if ask_change == "n":
            break
        elif ask_change ==  "y":
           continue
    else:
        word_convert = input("Enter word to change into: ")
        number_word_change = int(input("Number of word that will change:"))
        #convert string to list for better iteration
        paragraph_list = paragraph_input.split()

        #loop through the list of words to search and change
        for i in range (0,len(paragraph_list)):
            if i <= number_word_change:
                if  paragraph_list[i]==word_search :
                    paragraph_list[i]=word_convert
                count+=1
            else:
                break
        yes_no = 1

#Output
#function convert list to str
def listToString(paragraph):
    new_paragraph= " ".join(map(str,paragraph))
    return new_paragraph
print(listToString(paragraph_list))