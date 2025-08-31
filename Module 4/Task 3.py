smallest = None
largest = None

no = input("Enter a number: ")
while no != "":
    number = float(no)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
    no = input("Enter a number: ")

if smallest is None :
    print("no number found")
else :
    print("smallest is ", smallest)
    print("largest is ", largest)


