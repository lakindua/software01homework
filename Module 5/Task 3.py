number = int(input("Enter a number: "))
prime = []


for i in range(1,number+1):
    if number % i == 0:
        prime.append(i)


if number <= 2:
    print("Not a prime number")
elif len(prime) == 2:
    print("prime number")
else :
    print("Not a prime number")