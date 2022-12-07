f = open("input.txt", "r")
f = f.read()

i = -1
buffer_set = {}
while len(buffer_set) != 4:
	buffer = f[i:i + 4]
	buffer_set = set(buffer)
	i += 1

print(i + 3)