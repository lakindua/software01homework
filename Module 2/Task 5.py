talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

grams_per_lot = 13.3

total_lots = (talents * (32*20)+pounds*32 + lots)
total_grams = total_lots * grams_per_lot

kilograms = int(total_grams / 1000)
grams = total_grams % 1000  # to get the remainder

print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams")