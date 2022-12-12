class Node:
    def __init__(self, yPos, xPos):
        self.yPos = yPos
        self.xPos = xPos

    def __eq__(self, other):
        return self.yPos == other.yPos and self.xPos == other.xPos

    def __hash__(self):
        return hash(('yPos', self.yPos, 'xPos', self.xPos))
    
    def changePos(self, yPosDelta, xPosDelta):
        self.yPos += yPosDelta
        self.xPos += xPosDelta
    
    def nodeIsDifferent(self, yPos, xPos):
        return self.yPos != yPos or self.xPos != xPos

def moveHead(direction, currentYPos, currentXPos):
    newYPos = currentYPos
    newXPos = currentXPos
    if direction == "U":
        newYPos += 1
    elif direction == "D":
        newYPos -= 1
    elif direction == "R":
        newXPos += 1
    elif direction == "L":
        newXPos -= 1    
    return Node(newYPos, newXPos)

def createFollowingPath(path):
    currentKnotPos = Node(0,0)
    nodesKnotVisited = []
    nodesKnotVisited.append(Node(0,0))

    for step in path:
        if abs(step.xPos - currentKnotPos.xPos) > 1 and abs(step.yPos - currentKnotPos.yPos) > 1:
            if step.xPos > currentKnotPos.xPos:
                currentKnotPos.changePos(0, 1)
            else:
                currentKnotPos.changePos(0, -1)
            if step.yPos > currentKnotPos.yPos:
                currentKnotPos.changePos(1, 0)
            else:
                currentKnotPos.changePos(-1, 0)
        elif abs(step.xPos - currentKnotPos.xPos) > 1:      
            if step.xPos > currentKnotPos.xPos:
                currentKnotPos.changePos(step.yPos - currentKnotPos.yPos, 1)
            else:
                currentKnotPos.changePos(step.yPos - currentKnotPos.yPos, -1)
        elif abs(step.yPos - currentKnotPos.yPos) > 1:      
            if step.yPos > currentKnotPos.yPos:
                currentKnotPos.changePos(1, step.xPos - currentKnotPos.xPos)
            else:
                currentKnotPos.changePos(-1, step.xPos - currentKnotPos.xPos)
        if nodesKnotVisited[len(nodesKnotVisited)-1].nodeIsDifferent(currentKnotPos.yPos, currentKnotPos.xPos):
            nodesKnotVisited.append(Node(currentKnotPos.yPos, currentKnotPos.xPos))

    return nodesKnotVisited


headPath = []
headPath.append(Node(0, 0))

for item in open('input.txt', 'r'):
    for move in range(int(item.strip().split()[1])):
        headPath.append(moveHead(item.strip().split()[0], headPath[len(headPath)-1].yPos, headPath[len(headPath)-1].xPos))

knotPaths = []
knotPaths.append(headPath)

for knotNumber in range(9):
    print(len(set(knotPaths[len(knotPaths)-1])))
    knotPaths.append(createFollowingPath(knotPaths[knotNumber]))
    

print(len(set(knotPaths[len(knotPaths)-1])))
            
