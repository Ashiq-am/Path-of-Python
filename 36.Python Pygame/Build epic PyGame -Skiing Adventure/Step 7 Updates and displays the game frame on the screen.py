def updateFrame(screen, obstacles, skier):
	screen.fill((255, 255, 255))
	obstacles.draw(screen)
	screen.blit(skier.image, skier.rect)
	showScore(screen, skier.score)
	pygame.display.update()
