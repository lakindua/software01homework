airport = {"EFHK":"HELSINKI VANTAA AIRPORT", "EGLL":"LONDON HEAHROW AIRPORT", "OMDB":"DUBAI AIRPORT"}

print("Choose a option")
print("1- To add a new airport")
print("2- To fetch information of airport")

user_input = int(input("Your choice: "))

if user_input == 1:
    icao = input("Enter icao code : ").upper()
    airportname = input("Enter airport name : ").upper()
    airport[icao] = airportname
    print(airport)

elif user_input == 2:
    icao = input("Enter icao code to fetch information : ").upper()
    if icao in airport:
        print(airport[icao])
    else:
        print("Invalid icao code")

else:
    print("Invalid input")