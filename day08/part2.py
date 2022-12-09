import numpy
import copy
f = open("input.txt", "r")
f = f.read()
tree_grid = [list(x) for x in f.split('\n')]
tree_grid_t = numpy.transpose(tree_grid)

sy = 0
highest_score = 0
for row in tree_grid:
	sx = 0
	for col in tree_grid:
		num = tree_grid[sy][sx]
		row = copy.copy(tree_grid[sy])
		row_left = row[:sx][::-1]
		row_right = row[sx + 1:]

		col = list(copy.copy(tree_grid_t[sx]))
		col_top = col[:sy][::-1]
		col_bottom = col[sy + 1:]

		#print(row_left, row_right, col_top, col_bottom)
		view_a = 0
		for n in row_left:
			view_a += 1
			if n >= num:
				break

		view_b = 0
		for n in row_right:
			view_b += 1
			if n >= num:
				break

		view_c = 0
		for n in col_top:
			view_c += 1
			if n >= num:
				break

		view_d = 0
		for n in col_bottom:
			view_d += 1
			if n >= num:
				break

		scenic_score = view_a * view_b * view_c * view_d
		if scenic_score > highest_score:
			highest_score = scenic_score
		sx += 1
	sy += 1


print(highest_score)

