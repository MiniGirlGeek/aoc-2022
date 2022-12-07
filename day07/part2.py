import re
f = open("input.txt", "r")

class File:
	def __init__(self, parent, size, name):
		self.parent = parent
		self.size = size
		self.name = name
		self.parent.add_child(self)

class Directory:
	directories = []
	total_size = 0
	def __init__(self, parent, name):
		self.parent = parent
		self.name = name
		self.children = {}
		self.total_size = 0
		Directory.directories.append(self)

	def add_child(self, child):
		if type(child) == File:
			Directory.total_size += child.size
			c_dir = self
			while c_dir.parent != None:
				c_dir.total_size += child.size
				c_dir = c_dir.parent
			c_dir.total_size += child.size
			c_dir = c_dir.parent
			
		self.children[child.name] = child

change_directory = re.compile("\$ cd (.+)")
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

required_space = 30000000
current_space  = 70000000 - Directory.total_size
deletion_quantity = required_space - current_space
print(deletion_quantity)

answer = float('inf')
for directory in Directory.directories:
	size = directory.total_size
	if size < answer and size >= deletion_quantity:
		answer = size

print(answer)