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

path = []
path.append(Node(0, 0))

for item in open('input.txt', 'r'):
    for move in range(int(item.strip().split()[1])):
        path.append(moveHead(item.strip().split()[0], path[len(path)-1].yPos, path[len(path)-1].xPos))

print(len(path))

currentTailPos = Node(0, 0)
nodesTailVisited = []
nodesTailVisited.append(Node(0, 0))

for step in path:
    if abs(step.xPos - currentTailPos.xPos) > 1:      
        if step.xPos > currentTailPos.xPos:
            currentTailPos.changePos(step.yPos - currentTailPos.yPos, 1)
        else:
            currentTailPos.changePos(step.yPos - currentTailPos.yPos, -1)
    elif abs(step.yPos - currentTailPos.yPos) > 1:      
        if step.yPos > currentTailPos.yPos:
            currentTailPos.changePos(1, step.xPos - currentTailPos.xPos)
        else:
            currentTailPos.changePos(-1, step.xPos - currentTailPos.xPos)
    if nodesTailVisited[len(nodesTailVisited)-1].nodeIsDifferent(currentTailPos.yPos, currentTailPos.xPos):
        nodesTailVisited.append(Node(currentTailPos.yPos, currentTailPos.xPos))
    
print(len(set(nodesTailVisited)))
            
