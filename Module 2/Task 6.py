import random

code3 = [random.randint(0, 9) for _ in range(3)]

code4 = [random.randint(1, 6) for _ in range(4)]

print("3-digit code:", code3)
print("4-digit code:", code4)