myScore = 0

for line in open('input.txt', 'r'):
	result = line.strip()	
	if result == "A X":
		myScore += (1 + 3)
	elif result == "A Y":
		myScore += (2 + 6)
	elif result == "A Z":
		myScore += (3 + 0)
	elif result == "B X":
		myScore += (1 + 0)
	elif result == "B Y":
		myScore += (2 + 3)
	elif result == "B Z":
		myScore += (3 + 6)
	elif result == "C X":
		myScore += (1 + 6)
	elif result == "C Y":
		myScore += (2 + 0)
	elif result == "C Z":
		myScore += (3 + 3)
	else:
		myScore += 0

print(myScore)