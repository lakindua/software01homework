import random

def dice_roll(sides):
    return random.randint(1, sides)

user_input = int(input("How many sides : "))

result = dice_roll(user_input)
while result != user_input:
    result = dice_roll(user_input)
    print(result)