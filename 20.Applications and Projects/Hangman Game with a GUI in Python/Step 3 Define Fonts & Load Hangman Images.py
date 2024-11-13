# Fonts
font = pygame.font.SysFont("comicsans", 45)
WORD = pygame.font.SysFont("comicsans", 40)
TITLE = pygame.font.SysFont("comicsans", 70)

# Time to load images so we can draw a hangman
images = []
for i in range(0, 7):
	image = pygame.image.load("man" + str(i + 1) + ".png")
	images.append(image)

print(images)
