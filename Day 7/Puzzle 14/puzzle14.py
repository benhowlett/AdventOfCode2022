class Directory:
    def __init__(self, name):
        self.name = name
        self.subDirectories = []
        self.files = []
        self.allDirectorySizes = []

    def addSubDirectory(self, subDirectoryName):
        self.subDirectories.append(Directory(subDirectoryName))

    def addFile(self, file):
        self.files.append(file)

    def getFilesSize(self):
        sumOfFileSizes = 0
        for file in self.files:
            sumOfFileSizes += file.size
        return sumOfFileSizes
    
    def getTotalDirectorySize(self):
        directorySize = self.getFilesSize()
        for subDirectory in self.subDirectories:
            directorySize += subDirectory.getTotalDirectorySize()
        return directorySize

    def getSubdirectoryByName(self, subDirectoryName):
        for subDirectory in self.subDirectories:
            if subDirectory.name == subDirectoryName:
                return subDirectory

    def traverseDirectoryAndGetSizes(self):
        self.allDirectorySizes.append(self.getTotalDirectorySize())
        for subDirectory in self.subDirectories:
            subDirectory.traverseDirectoryAndGetSizes()
            for size in subDirectory.allDirectorySizes:
                self.allDirectorySizes.append(size)
    
    def getSumOfAllDirectorySizes(self):
        total = 0
        for size in self.allDirectorySizes:
            total += size
        return total

  

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


root = Directory("/")
currentDirectory = root
path = []
directorySizes = []
currentlyListing = False

for line in open('input.txt', 'r'):

    if line.split()[0] == "$":

        if line.split()[1] == "cd":

            if line.split()[2] == "..":
                path.pop()
                tempDirectory = root
                for step in path:
                    tempDirectory = tempDirectory.getSubdirectoryByName(step)
                currentDirectory = tempDirectory
            
            elif line.split()[2] == "/":
                currentDirectory = root

            else:
                currentDirectory = currentDirectory.getSubdirectoryByName(line.split()[2])
                path.append(line.split()[2])
    else:

        if line.split()[0] == "dir":

            currentDirectory.addSubDirectory(line.split()[1])

        else:

            currentDirectory.addFile(File(line.split()[1], int(line.split()[0])))

root.traverseDirectoryAndGetSizes()

target = root.getTotalDirectorySize() - 40000000

largeEnoughDirectories = []

for size in root.allDirectorySizes:
    if size >= target:
        largeEnoughDirectories.append(size)

print(sorted(largeEnoughDirectories)[0])
         