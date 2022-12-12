stack1 = ['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T']
stack2 = ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V']
stack3 = ['B', 'J', 'F', 'H', 'D', 'R', 'P']
stack4 = ['F', 'R', 'P', 'B', 'M', 'N', 'D']
stack5 = ['H', 'V', 'R', 'P', 'T', 'B']
stack6 = ['C', 'B', 'P', 'T']
stack7 = ['B', 'J', 'R', 'P', 'L']
stack8 = ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W']
stack9 = ['L', 'S', 'G']

def moveBoxes(numberOfBoxes, fromStack, toStack):
    tempBoxes = []
    for box in range(int(numberOfBoxes)):
        tempBoxes.append(globals()['stack'+fromStack].pop())       
    for box in reversed(tempBoxes):
        globals()['stack'+toStack].append(box)

for item in open('instructions.txt', 'r'):
    moveBoxes(item.strip().split()[1], item.strip().split()[3], item.strip().split()[5])

print(stack1[len(stack1)-1], stack2[len(stack2)-1], stack3[len(stack3)-1], stack4[len(stack4)-1], stack5[len(stack5)-1], stack6[len(stack6)-1], stack7[len(stack7)-1], stack8[len(stack8)-1], stack9[len(stack9)-1])
