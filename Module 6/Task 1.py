import random

def dice_roll():
    return random.randint(1, 6)

result = 0
while result != 6:
    result = dice_roll()
    print(result)



