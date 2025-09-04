import random

dice = input("How many dice should roll: ")
no = random.randint(1,7)
num = []

for i in range(0,int(dice)):
    num.append(random.randint(1,7))

print(sum(num))

