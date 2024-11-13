# Initialize pygame and set the colors with captions
pygame.init()

# Define color codes
gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

# Define display dimensions
display_width = 800
display_height = 600

# Set up game display
gamedisplays = pygame.display.set_mode((display_width,
										display_height))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()

# Load car image and background images
carimg = pygame.image.load('car1.jpg')
backgroundpic = pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.jpg")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("background.jpg")
instruction_background = pygame.image.load("background2.jpg")

# Set car width and initialize pause state
car_width = 56
pause = False
