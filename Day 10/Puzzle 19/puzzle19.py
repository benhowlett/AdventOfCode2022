cycles = 0
signal = 1
signalStrengths = []

def checkSignalStrength(cycles, signal):
    if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
        return cycles * signal

for line in open('input.txt', 'r'):
    cycles += 1
    signalStrengths.append(checkSignalStrength(cycles, signal))
    if line.strip().split()[0] == "addx":
        cycles += 1
        signalStrengths.append(checkSignalStrength(cycles, signal))
        signal += int(line.strip().split()[1])

totalSignalStrength = 0

for item in signalStrengths:
    if item != None:
        totalSignalStrength += item

print(totalSignalStrength)


        