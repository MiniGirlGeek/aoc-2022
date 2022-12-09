import numpy
import copy
f = open("input.txt", "r")
f = f.read()
tree_grid = [list(x) for x in f.split('\n')]
tree_grid_t = numpy.transpose(tree_grid)

search_grid = []
for row in tree_grid[1:-1]:
	search_grid.append(row[1:-1])


sy = 0
no_visible = len(tree_grid) * 2 + len(tree_grid[0]) * 2 - 4
for row in search_grid:
	sx = 0
	for col in search_grid:
		num = search_grid[sy][sx]
		row = copy.copy(tree_grid[sy + 1])
		row_left = set(row[:sx + 1])
		row_right = set(row[sx + 2:])

		col = list(copy.copy(tree_grid_t[sx + 1]))
		col_top = set(col[:sy + 1])
		col_bottom = set(col[sy + 2:])

		

		for n in row_left:
			if n >= num:
				visible = False
				break
			else: 
				visible = True

		if not visible:
			for n in row_right:
				if n >= num:
					visible = False
					break
				else: 
					visible = True

			if not visible:
				for n in col_top:
					if n >= num:
						visible = False
						break
					else: 
						visible = True
				if not visible:
					for n in col_bottom:
						if n >= num:
							visible = False
							break
						else: 
							visible = True
		if visible:
			no_visible += 1
		sx += 1
	sy += 1

print(no_visible)
