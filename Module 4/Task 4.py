import random

number = random.randint(1,10)
user_no = None

while user_no != number :
    user_no = int(input("Enter a number between 1 and 10: "))
    if user_no < number :
        print("Too low")
    elif user_no > number :
        print("Too high")
    else:
        print("correct")