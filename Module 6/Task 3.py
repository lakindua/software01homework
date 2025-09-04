def convo(lit):
    return lit*3.785

gasoline = float(input("Input volume of gasoline in gallons: "))
result = convo(gasoline)

if result < 0:
   print("Invalid input")
else:
   print(result)