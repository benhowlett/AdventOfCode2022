trees = []
largestScenicScore = 0

for line in open('input.txt', 'r'):
    row = []
    for item in line.strip():
        row.append(int(item))
    trees.append(row)

for row in range(len(trees)):
    for column in range(len(trees[row])): 
        north = []                                      # check trees to the north
        for tempRow in range(row):
            north.append(trees[tempRow][column])
        north.reverse()
        northScore = 0
        for tree in north:
            if tree >= trees[row][column]:
                northScore += 1
                # print("North score: " + str(northScore))
                break
            else:
                northScore += 1
        
        south = []                                      # check trees to the south
        for tempRow in range(row+1, len(trees)):
            south.append(trees[tempRow][column])
        southScore = 0
        for tree in south:
            if tree >= trees[row][column]:
                southScore += 1
                # print("South score: " + str(southScore))
                break
            else:
                southScore += 1

        east = []                                      # check trees to the east
        for tempColumn in range(column+1, len(trees[row])):
            east.append(trees[row][tempColumn])
        eastScore = 0
        for tree in east:
            if tree >= trees[row][column]:
                eastScore += 1
                # print("East score: " + str(eastScore))
                break
            else:
                eastScore += 1
        
        west = []                                      # check trees to the west
        for tempColumn in range(column):
            west.append(trees[row][tempColumn])
        west.reverse()
        westScore = 0
        for tree in west:
            if tree >= trees[row][column]:
                westScore += 1
                # print("West score: " + str(westScore))
                break
            else:
                westScore += 1

        #print("Largest Scenic Score: " + str(largestScenicScore))
        #print("Current Scenic Score: " + str(northScore * southScore * eastScore * westScore))
        if (northScore * southScore * eastScore * westScore) > largestScenicScore:
            largestScenicScore = northScore * southScore * eastScore * westScore
        #print("Largest Scenic Score: " + str(largestScenicScore))

print(largestScenicScore)
                       