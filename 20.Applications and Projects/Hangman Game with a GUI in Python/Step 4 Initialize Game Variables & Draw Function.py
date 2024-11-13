# Game variables
hangman = 0
lists = ["GEEKS", "GFG", "DOCKER", "DEVELOPER", "RUST", "GITHUB", "R", "PYTHON", "BASH"]
words = random.choice(lists)
guessed = [] # to track the letters we have guessed

# Function to draw buttons, and hangman
def draw():
	win.fill((255, 255, 255)) # Display with white color

	# Title for the game
	# Updated title for better visibility
	title = TITLE.render("Hangman", 1, (0, 0, 0))
	# Title in center and then y-axis= 24
	win.blit(title, (WIDTH/1.7 - title.get_width() / 2, 10))

	# Draw word on the screen
	disp_word = ""
	for letter in words:
		if letter in guessed:
			disp_word += letter + " "
		else:
			disp_word += "_ "

	text = WORD.render(disp_word, 1, (0, 0, 0))
	win.blit(text, (500, 250))

	# Buttons at center
	for btn_pos in letters:
	# Making button visible and invisible after clicking it
		x, y, ltr, visible = btn_pos

		if visible:
			pygame.draw.circle(win, (0, 0, 0), (x, y), radius, 4)
			txt = font.render(ltr, 1, (0, 0, 0))
			win.blit(txt, (x - txt.get_width() / 2, y - txt.get_height() / 2))

	win.blit(images[hangman], (50, 50))
	pygame.display.update()
