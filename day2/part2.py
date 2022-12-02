# A, X = Rock, B, Y = Paper, C, Z = Scissors
# AX beats CZ, CZ beats BY, BY beats AX
f = open("input.txt", "r")
rounds = f.read().split("\n")

num       = {"A": 0, "B": 1,"C": 2}
scenarios = {"X": 2, "Y": 3,"Z": 1}

your_choices = ["A", "B", "C"]

score1 = {
	"A": 1,
	"B": 2,
	"C": 3,
}

score2 = {
	"X": 0,
	"Y": 3,
	"Z": 6
}

score = 0
for r in rounds:
	elf, scenario = r.split(" ")
	elf_num = num[elf]
	choice = your_choices[(elf_num + scenarios[scenario]) % 3]
	score += score1[choice] + score2[scenario]
print(score)