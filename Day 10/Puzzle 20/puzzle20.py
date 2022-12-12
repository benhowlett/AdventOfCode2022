cycles = 0
spritePos = 2
screen = []
row = []

def checkSpritePos(cycles, spritePos):
    return cycles % 40 >= spritePos - 1 and cycles % 40 <= spritePos + 1

def writeToScreen(row):
    if len(row) == 40:
        screen.append(row)
        row = []
    
    if checkSpritePos(cycles, spritePos):
        row.append("#")
    else:
        row.append(".")
    
    return row

for line in open('input.txt', 'r'):
    cycles += 1

    row = writeToScreen(row)
    
    if line.strip().split()[0] == "addx":
        cycles += 1
        row = writeToScreen(row)
        spritePos += int(line.strip().split()[1])

screen.append(row)

for row in screen:
    rowStr = ""
    for item in row:
        rowStr += item
    print(rowStr)

        