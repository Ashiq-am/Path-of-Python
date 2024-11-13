import pygame
# initializing the pygame
pygame.init()
# displaying Canvas (960*600)
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption('GeeksForGeeks')
clock = pygame.time.Clock()

loop = True
while loop:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
	pos = pygame.mouse.get_pos()
	# giving color and shape to the circle
	pygame.draw.circle(screen, (0, 255, 0),
					pos, 15, 1)
	pygame.display.update()
	clock.tick(60)


pygame.quit()
# quit()
