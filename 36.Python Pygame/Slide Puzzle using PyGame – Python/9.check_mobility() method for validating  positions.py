# check if the tile can be placed
# in the required position where
# the player is trying to move the tile


def check_mobility():
	for i in range(tile_count):
		tile = tiles[i]
		row_index = tile.position_x
		col_index = tile.position_y
		adjacent_cells = []
		adjacent_cells.append([row_index-1, col_index, False]) # up
		adjacent_cells.append([row_index+1, col_index, False]) # down
		adjacent_cells.append([row_index, col_index-1, False]) # right
		adjacent_cells.append([row_index, col_index+1, False]) # left
		for i in range(len(adjacent_cells)):
			if (adjacent_cells[i][0] >= 0 and adjacent_cells[i][0] < rows) and (adjacent_cells[i][1] >= 0 and adjacent_cells[i][1] < cols):
				adjacent_cells[i][2] = True

		for j in range(len(adjacent_cells)):
			if adjacent_cells[j][2]:
				adj_cell_row = adjacent_cells[j][0]
				adj_cell_col = adjacent_cells[j][1]
				for k in range(tile_count):
					if adj_cell_row == tiles[k].position_x and adj_cell_col == tiles[k].position_y:
						adjacent_cells[j][2] = False

				false_count = 0

				for m in range(len(adjacent_cells)):
					if adjacent_cells[m][2]:
						tile.movable = True
						break
					else:
						false_count += 1

				if false_count == 4:
					tile.movable = False
