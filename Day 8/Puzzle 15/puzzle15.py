trees = []
countOfVisible = 0

for line in open('input.txt', 'r'):
    row = []
    for item in line.strip():
        row.append(int(item))
    trees.append(row)

for row in range(len(trees)):
    for column in range(len(trees[row])): 
        if row == 0 or row == len(trees) - 1:               # count all trees in the outer 2 rows
            countOfVisible += 1
        elif column == 0 or column == len(trees[row]) - 1:   # count all trees in the outer 2 columns
            countOfVisible += 1
        else:                                               # determine if any interior trees are visible
            north = []                                      # check trees to the north
            isVisible = True
            for tempRow in range(row):
                north.append(trees[tempRow][column])
            for tree in north:
                if tree >= trees[row][column]:
                    isVisible = False
            if isVisible: 
                countOfVisible += 1
            else:
                south = []                                      # check trees to the south
                isVisible = True
                for tree in range(row+1, len(trees)):
                    south.append(trees[tree][column])
                for tree in south:
                    if tree >= trees[row][column]:
                        isVisible = False
                if isVisible: 
                    countOfVisible += 1
                else:
                    east = []                                      # check trees to the east
                    isVisible = True
                    for tree in range(column+1, len(trees[row])):
                        east.append(trees[row][tree])
                    for tree in east:
                        if tree >= trees[row][column]:
                            isVisible = False
                    if isVisible: 
                        countOfVisible += 1
                    else:
                        west = []                                      # check trees to the west
                        isVisible = True
                        for tree in range(column):
                            west.append(trees[row][tree])
                        for tree in west:
                            if tree >= trees[row][column]:
                                isVisible = False
                        if isVisible: 
                            countOfVisible += 1

print(countOfVisible)

        