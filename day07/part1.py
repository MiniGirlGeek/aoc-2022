import re
f = open("input.txt", "r")

class File:
	def __init__(self, parent, size, name):
		self.parent = parent
		self.size = size
		self.name = name
		self.parent.add_child(self)

class Directory:
	below_100000 = []
	def __init__(self, parent, name):
		self.parent = parent
		self.name = name
		self.children = {}
		self.total_size = 0
		Directory.below_100000.append(self)

	def add_child(self, child):
		if type(child) == File:
			c_dir = self
			while c_dir.parent != None:
				c_dir.total_size += child.size
				if c_dir.total_size > 100000:
					if c_dir in Directory.below_100000:
						Directory.below_100000.remove(c_dir)
				c_dir = c_dir.parent
			
		self.children[child.name] = child

change_directory = re.compile("\$ cd (.+)")
list_files = re.compile("\$ ls")
file_line = re.compile("([0-9]+) (.+)") 

parent = None
current_dir = None
EOF = False
while EOF == False:
	line = f.readline()
	if line == "":
		EOF = True
	cd = change_directory.match(line)
	file = file_line.match(line)
	if cd:
		if cd[1] == "..":
			current_dir = current_dir.parent
		else:
			current_dir = Directory(current_dir, cd[1])
	if file:
		new_file = File(current_dir, int(file[1]), file[2])

answer = 0
for dir in Directory.below_100000:
	answer += dir.total_size

print(answer)

