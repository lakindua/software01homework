cabin = input(str("Enter the cabin class : ")).lower()
if cabin == "lux":
    print("your cabin class is in the upper-deck cabin with a balcony.")
elif cabin == "a":
    print("your cabin class is in above the car deck, equipped with a window.")
elif cabin == "b":
    print("your cabin class is the windowless cabin above the car deck.")
elif cabin == "c":
    print("your cabin class is the windowless cabin below the car deck.")
else:
    print("Invalid cabin class")