myScore = 0

loseResult = {
	"A": 3,
	"B": 1,
	"C": 2
}

tieResult = {
	"A": 4,
	"B": 5,
	"C": 6
}

winResult = {
	"A": 8,
	"B": 9,
	"C": 7
}

def matchResult(opponent, outcome):
	if outcome == "X":
		return loseResult[opponent]
	elif outcome == "Y":
		return tieResult[opponent]
	else:
		return winResult[opponent]

for line in open('input.txt', 'r'):
	myScore += matchResult(line.strip().split()[0], line.strip().split()[1])

print(myScore)