def rangesOverlap(firstRange, secondRange):
    if int(firstRange[0]) <= int(secondRange[0]) and int(firstRange[1]) >= int(secondRange[1]):
        return True
    elif int(firstRange[0]) >= int(secondRange[0]) and int(firstRange[1]) <= int(secondRange[1]):
        return True
    elif int(firstRange[1]) >= int(secondRange[0]) and int(firstRange[0]) <= int(secondRange[1]):
        return True
    else:
        return False

fullyContainedCount = 0

for line in open("input.txt", "r"):
    print(line.strip().split(',')[0].split('-'), line.strip().split(',')[1].split('-'))
    if rangesOverlap(line.strip().split(',')[0].split('-'), line.strip().split(',')[1].split('-')):
        fullyContainedCount += 1

print(fullyContainedCount)