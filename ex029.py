numbers = [5, 2, 2, 7, 4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)