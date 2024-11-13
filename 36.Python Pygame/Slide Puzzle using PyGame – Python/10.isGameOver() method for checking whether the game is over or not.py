# if after iterating the matrix
# the string we get is 12345678_
# then the player has won("Game Over")


def isGameOver():
	global game_over, game_over_banner
	allcelldata = ""
	for i in range(rows):
		for j in range(cols):
			allcelldata = allcelldata + str(matrix[i][j])

	if allcelldata == "12345678 ":
		game_over = True
		game_over_banner = "Game Over"

		print("Game Over")
		# lock the tiles at that position
		for i in range(tile_count):
			tiles[i].movable = False
			tiles[i].selected = False
