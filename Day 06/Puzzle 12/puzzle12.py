def allItemsAreUnique(list):
    areUnique = True
    for item in list:
        if list.count(item) > 1:
            areUnique = False
    return areUnique

dataStream = open('input.txt', 'r').readline()

firstMarkerPosition = 0
rollingBuffer = []

for item in dataStream:
    if len(rollingBuffer) == 14:
        if allItemsAreUnique(rollingBuffer):
            break
        del rollingBuffer[0]
    rollingBuffer.append(item) 
    firstMarkerPosition += 1   
    

print(firstMarkerPosition)