correct_username = "python"
correct_password = "rules"
attempts = 0


while 5 > attempts :
    username = input("Enter a username: ")
    password = input("Enter a password: ")


    if username == correct_username and password == correct_password :
        print("Login Successful")
        break
    else:
        print("Invalid Username or Password.Try Again!")
        attempts += 1

if attempts == 5 :
    print("You have reached the maximum number of attempts")


