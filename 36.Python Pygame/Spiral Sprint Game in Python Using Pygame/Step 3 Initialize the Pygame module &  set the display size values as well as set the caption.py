# initialize pygame and set the display size and alignment
pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
CENTER = WIDTH // 2, HEIGHT // 2
info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(
		SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption('Connected')
