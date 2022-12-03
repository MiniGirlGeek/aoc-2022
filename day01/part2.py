f = open("input.txt", "r")
f = f.read()
elves = f.split("\n\n")

most_calories = [0, 0, 0]
for elf in elves:
	food_items = elf.split('\n')
	total_calories = 0
	for food in food_items:
		total_calories += int(food)
	if most_calories[2] < total_calories:
		most_calories = most_calories[1:3]
		most_calories.append(total_calories)
	elif most_calories[1] < total_calories:
		most_calories[0] = most_calories[1]
		most_calories[1] = total_calories
	elif most_calories[0] < total_calories:
		most_calories[0] = total_calories
print(most_calories)
print(most_calories[0] + most_calories[1] + most_calories[2])