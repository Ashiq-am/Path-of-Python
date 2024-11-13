# Create tiles w.r.t to no of tiles available
def create_tyles():
	i = 1
	# create tiles at random positions
	while i <= tile_count:
		r = random.randint(1, tile_count)
		if r not in tile_no:
			tile_no.append(r)
			i += 1
	tile_no.append("")
	k = 0
	# print the tiles in the grid
	for i in range(0, rows):
		for j in range(0, cols):
			if (i == rows - 1) and (j == cols - 1):
				pass
			else:
				t = Tiles(screen, tile_print_position[(
					i, j)][0], tile_print_position[(i, j)][1],
						tile_no[k], i, j)
				tiles.append(t)
			matrix[i][j] = tile_no[k]
			k += 1
	check_mobility()
