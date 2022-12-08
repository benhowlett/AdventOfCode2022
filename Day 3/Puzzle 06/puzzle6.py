def checkForBadge(elfOne, elfTwo, elfThree):
    for elfOneItem in elfOne:
        for elfTwoItem in elfTwo:
            for elfThreeItem in elfThree:
                if elfOneItem == elfTwoItem == elfThreeItem:
                    return elfOneItem

def calculatePriority(item):
    if ord(item) > 90:
        return ord(item) - 96
    else:
        return ord(item) - 38

prioritySum = 0
elfRucksacks = []

for rucksack in open("input.txt", "r"):
    elfRucksacks.append(rucksack)
    if len(elfRucksacks) == 3:
        prioritySum += calculatePriority(checkForBadge(elfRucksacks[0], elfRucksacks[1], elfRucksacks[2]))
        elfRucksacks = []

print(prioritySum)