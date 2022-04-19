weight = input("Please enter your weight: ")
unit = input("(L)bs or (K)g: ")
if unit == "L":
    converted = float(weight) * 0.45
    print(f"Your weight in kg is {converted}")
elif unit == "K":
    converted = float(weight) / 0.45
    print(f"Your weight in lbs is {converted}")
else:  
    print("Please enter L or K")