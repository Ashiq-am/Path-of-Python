def show_score(x, y):
	score = font.render("Points: " + str(score_val),
						True, (255, 255, 255))
	screen.blit(score, (x, y))
