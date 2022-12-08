input = open('input.txt', 'r')
calories = 0
calorieTotals = []

for line in input:
    if line.strip() == '':
        calorieTotals.append(calories)
        calories = 0
    else:
        calories += int(line.strip())

calorieTotals.sort(reverse=True)

print(calorieTotals[0])

