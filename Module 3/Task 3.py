gender = str(input("Enter your gender: ")).lower()
hemo = float(input("Enter your hemoglobin level: "))

if gender == "male" and 134 <= hemo <= 167 :
    print("Your hemoglobin level is good")
elif gender == "male" and 134 > hemo :
    print("Your hemoglobin level is low")
elif gender == "male" and hemo > 167 :
    print("Your hemoglobin level is high")
if gender == "female" and 117 <= hemo <= 155 :
    print("Your hemoglobin level is good")
elif gender == "female" and 117 > hemo :
    print("Your hemoglobin level is low")
elif gender == "female" and hemo > 155 :
    print("Your hemoglobin level is high")
else:
    print("Invalid input")

