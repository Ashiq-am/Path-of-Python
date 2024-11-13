def showScore(screen, score, pos=(10, 10)):
	font = pygame.font.Font(cfg.FONTPATH, 30)
	score_text = font.render("Score: %s" % score, True, (0, 0, 0))
	screen.blit(score_text, pos)
