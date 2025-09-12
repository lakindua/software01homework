seasons = ("winter", "spring", "summer", "autumn")

user_input = int(input("Enter the number of month : "))

if user_input == 12 or user_input == 1 or user_input == 2:
    season = seasons[0]
elif user_input == 3 or user_input == 4 or user_input == 5:
    season = seasons[1]
elif user_input == 6 or user_input == 7 or user_input == 8:
    season = seasons[2]
else:
    season = seasons[3]


print("The season is",season)