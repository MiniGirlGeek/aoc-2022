f = open("input.txt", "r")
f = f.read()
elves = f.split("\n\n")

most_calories = 0
for elf in elves:
	food_items = elf.split('\n')
	total_calories = 0
	for food in food_items:
		total_calories += int(food)
	if most_calories < total_calories:
		most_calories = total_calories

print(most_calories)