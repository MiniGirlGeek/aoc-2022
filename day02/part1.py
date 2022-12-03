# A, X = Rock, B, Y = Paper, C, Z = Scissors
# AX beats CZ, CZ beats BY, BY beats AX
f = open("input.txt", "r")
rounds = f.read().split("\n")

num = {
		"A": 0,
	 	"B": 1,
		"C": 2,
		"X": 0,
		"Y": 1,
		"Z": 2
}

score1 = {
	"X": 1,
	"Y": 2,
	"Z": 3,
}

score2 = {
	0: 3,
	1: 6,
	2: 0
}

score = 0
for r in rounds:
	elf, you = r.split(" ")
	elf_num = num[elf]
	you_num = num[you]
	result = (you_num - elf_num) % 3
	score += score1[you] + score2[result]
	print(score1[you] + score2[result])

print(score)