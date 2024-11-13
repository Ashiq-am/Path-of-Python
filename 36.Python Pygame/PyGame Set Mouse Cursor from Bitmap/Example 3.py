import pygame
pygame.init()

# Creating a canvas of 600*400
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# old type, "bitmap" cursor
cursor1 = pygame.cursors.diamond

# new type, "system" cursor
cursor2 = pygame.SYSTEM_CURSOR_HAND

# new type, "color" cursor
surf = pygame.Surface((30, 25), pygame.SRCALPHA)
pygame.draw.rect(surf, (0, 255, 0), [0, 0, 10, 10])
pygame.draw.rect(surf, (0, 255, 0), [20, 0, 10, 10])
pygame.draw.rect(surf, (255, 0, 0), [5, 5, 20, 20])
cursor3 = pygame.cursors.Cursor((15, 5), surf)

cursors = [cursor1, cursor2, cursor3]
cursor_index = 0

# the arguments to set_cursor can be a Cursor object
# or it will construct a Cursor object
# internally from the arguments
pygame.mouse.set_cursor(cursors[cursor_index])

while True:
	screen.fill("purple")

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			cursor_index += 1
			cursor_index %= len(cursors)
			pygame.mouse.set_cursor(cursors[cursor_index])

		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit

	pygame.display.flip()
	clock.tick(144)
