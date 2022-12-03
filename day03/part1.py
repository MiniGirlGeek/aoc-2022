f = open("input.txt", "r")
rucksacks = f.read().split("\n")

def get_priority(x):
	if x.islower():
		return ord(x) - 96
	else:
		return ord(x) - 38

priority_total = 0
for rucksack in rucksacks:
	size = len(rucksack)
	compartment1 = rucksack[0:size//2]
	compartment2 = rucksack[size//2::]
	for item in compartment1:
		if item in compartment2:
			priority_total += get_priority(item)
			break

print(priority_total)