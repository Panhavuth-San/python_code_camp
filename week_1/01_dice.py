import random
start=1
total=0
print("Welcome to the dices")

while start == 1:
    user_input = input("Enter the number of dices you want to roll: ")
    dices = int(user_input)
    if dices >=1  and dices <=8:
        for i in range(dices):
            number = random.randint(1,8)
            print("Dice",i+1," : ",number)
            total +=number
        print("="*10)
        print("RESULT:", total )
        print("="*10)
        start = 0
    else:
        print("USAGE: The number must be between 1 and 8")
        continue
