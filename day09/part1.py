f = open("input.txt", "r")
import math

H_x, H_y, T_x, T_y = 0, 0, 0, 0

tail_locations = {(T_x, T_y)}

def check_adjacent(H_x, H_y, T_x, T_y):
	adjacent = [[-1, -1], [ 0, -1], [ 1, -1],
				[-1,  0], [ 0,  0], [ 1,  0],
				[-1,  1], [ 0,  1], [ 1,  1]]
	x_diff = H_x - T_x
	y_diff = H_y - T_y

	if [x_diff, y_diff] in adjacent:
		return True
	return False

def tail_update(H_x, H_y, T_x, T_y):
	if H_x != T_x and H_y != T_y:
		if H_x > T_x:
			T_x += 1
		else:
			T_x -=1
		if H_y > T_y:
			T_y += 1
		else:
			T_y -= 1
	else:
		T_x += (H_x - T_x) // 2
		T_y += (H_y - T_y) // 2
	return T_x, T_y


grid = [["." for x in range(6)] for y in range(5)]

line = f.readline()
while line != "":
	direction, magnitute = line.split(" ")
	if direction == "L":
		for steps in range(int(magnitute)):
			H_x -= 1
			if not check_adjacent(H_x, H_y, T_x, T_y):
				T_x, T_y = tail_update(H_x, H_y, T_x, T_y)
				tail_locations.add((T_x, T_y))

	elif direction == "R":
		for steps in range(int(magnitute)):
			H_x += 1
			if not check_adjacent(H_x, H_y, T_x, T_y):
				T_x, T_y = tail_update(H_x, H_y, T_x, T_y)
				tail_locations.add((T_x, T_y))
	elif direction == "U":
		for steps in range(int(magnitute)):
			H_y += 1
			if not check_adjacent(H_x, H_y, T_x, T_y):
				T_x, T_y = tail_update(H_x, H_y, T_x, T_y)
				tail_locations.add((T_x, T_y))
	else:
		for steps in range(int(magnitute)):
			H_y -= 1
			if not check_adjacent(H_x, H_y, T_x, T_y):
				T_x, T_y = tail_update(H_x, H_y, T_x, T_y)
				tail_locations.add((T_x, T_y))
	line = f.readline()

print(len(tail_locations))