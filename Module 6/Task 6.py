import math

def pizza(price,dia):
    radi = (dia/2)/100
    area = math.pi*(radi**2)
    return price/area

user_input01 = float(input("Please enter your 1st pizza price: "))
user_input02 = float(input("Enter the diameter of 1st pizza in cm : "))
x = pizza(user_input01,user_input02)

user_input03 = float(input("Please enter your 2nd pizza price: "))
user_input04 = float(input("Enter the diameter of 2nd pizza in cm : "))
y = pizza(user_input03,user_input04)

if x < y:
   print("Your 1st pizza is the best option")
else:
    print("Your 2nd pizza is the best option")

