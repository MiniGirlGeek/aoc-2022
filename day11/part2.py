import re
import math
f = open("input.txt", "r")
monkey_parameters = f.read().split("\n\n")

class Monkey:
	monkey_number = re.compile("Monkey ([0-9]+):")
	starting_items = re.compile("  Starting items:( [0-9]+,*)+")
	operation = re.compile("  Operation: new = old ([\+\*]) ([old0-9]+)")
	test = re.compile("  Test: divisible by ([0-9]+)")
	true = re.compile("    If true: throw to monkey ([0-9]+)")
	false = re.compile("    If false: throw to monkey ([0-9]+)")
	numbers = re.compile("([0-9]+)")

	monkey_dictionary = {}
	monkey_list = []
	def __init__(self, parameters):
		self.number = int(Monkey.monkey_number.search(parameters)[1])
		Monkey.monkey_dictionary[self.number] = self
		Monkey.monkey_list.append(self)
		starting_items_line = Monkey.starting_items.search(parameters)[0]
		self.items = [int(x) for x in re.findall(Monkey.numbers, starting_items_line)]
		operation_line = Monkey.operation.search(parameters)
		self.operation = operation_line[1]
		self.operation_value = operation_line[2]
		self.test = Monkey.test.search(parameters)[1]
		self.true = int(Monkey.true.search(parameters)[1])
		self.false = int(Monkey.false.search(parameters)[1])
		self.inspections = 0

	def take_turn(self):
		for i in range(len(self.items)):
			self.inspections += 1
			if self.operation == "+":
				if self.operation_value == "old":
					self.items[i] = self.items[i] + self.items[i]
				else:
					self.items[i] = self.items[i] + int(self.operation_value)
			elif self.operation == "*":
				if self.operation_value == "old":
					self.items[i] = self.items[i] * self.items[i]
				else:
					self.items[i] = self.items[i] * int(self.operation_value)
			reduction = math.lcm(*[int(m.test) for m in Monkey.monkey_list])
			self.items[i] = self.items[i] % reduction
			if self.items[i] % int(self.test) == 0:
				Monkey.monkey_dictionary[int(self.true)].items.append(self.items[i])
			else:
				Monkey.monkey_dictionary[int(self.false)].items.append(self.items[i])
		self.items = []

	def __repr__(self):
		return str(self.inspections)



for monkey_parameter in monkey_parameters:
	Monkey(monkey_parameter)

for round in range(10000):
	for monkey in Monkey.monkey_list:
		monkey.take_turn()
	if round in [0, 999, 9999]:
		print(round, Monkey.monkey_list)