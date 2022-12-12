calories = 0
calorieTotals = []

for line in open('input.txt', 'r'):
    if line.strip() == '':
        calorieTotals.append(calories)
        calories = 0
    else:
        calories += int(line.strip())

calorieTotals.sort(reverse=True)

print(calorieTotals[0]+calorieTotals[1]+calorieTotals[2])
