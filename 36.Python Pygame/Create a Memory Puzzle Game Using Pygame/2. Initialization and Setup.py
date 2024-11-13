# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
CARD_SIZE = 175
GRID_SIZE = 4
WHITE = (255, 255, 255)
FLIP_DELAY = 0.5
BUTTON_WIDTH = 140
BLACK = (0, 0, 0)
BUTTON_HEIGHT = 40
TIMER_LIMIT = 15

# URLs for images
image_urls = [
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120810/f.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311121011/d.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/a.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/b.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120801/c.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122347/z.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/y.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/x.webp"
]

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")
