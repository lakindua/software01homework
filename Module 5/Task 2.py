number = []

for i in range(10**10):
    user_no = input("Enter your number: ")
    if user_no == "":
        break
    else :
        user_no = int(user_no)
        number.append(user_no)
        number.sort(reverse=True)

print(number[0:5])
