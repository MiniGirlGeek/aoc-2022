f = open("input.txt", "r")
elf_pairs = f.read().split("\n")

overlap = 0
for elf_pair in elf_pairs:
	elf1, elf2 = elf_pair.split(",")
	elf1 = [int(num) for num in elf1.split("-")]
	elf2 = [int(num) for num in elf2.split("-")]

	if ((elf1[0] <= elf2[0]) and (elf1[1] >= elf2[1])) or ((elf2[0] <= elf1[0]) and (elf2[1] >= elf1[1])):
		overlap += 1
	elif ((elf2[0] <= elf1[1]) and (elf2[1] >= elf1[0])) or ((elf1[0] <= elf2[1]) and (elf1[1] >= elf2[0])):
		overlap += 1
print(overlap)