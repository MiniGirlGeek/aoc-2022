f = open("input.txt", "r")
rucksacks = f.read().split("\n")

def get_priority(x):
	if x.islower():
		return ord(x) - 96
	else:
		return ord(x) - 38

gp = 0
priority_total = 0
while gp + 2 < len(rucksacks):
	r1 = rucksacks[gp]
	r2 = rucksacks[gp + 1]
	r3 = rucksacks[gp + 2]
	for item in r1:
		if (item in r2) and (item in r3):
			priority_total += get_priority(item)
			break
	gp += 3

print(priority_total)