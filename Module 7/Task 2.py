user_name = None

names = set()

while user_name != "":
    user_name = input("Enter the name of the person : ")

    if user_name != "":
        if user_name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(user_name)

for name in names:
    print(name)