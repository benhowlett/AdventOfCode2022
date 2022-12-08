def checkCompartmentContent(compartmentOne, compartmentTwo):
    for compartmentOneItem in compartmentOne:
        for compartmentTwoItem in compartmentTwo:
            if compartmentOneItem == compartmentTwoItem:
                return compartmentOneItem

def calculatePriority(item):
    if ord(item) > 90:
        return ord(item) - 96
    else:
        return ord(item) - 38

prioritySum = 0

for rucksack in open("input.txt", "r"):
    prioritySum += calculatePriority(checkCompartmentContent(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]))

print(prioritySum)