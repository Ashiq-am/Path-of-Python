import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Sample")

# Set up colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the initial position and speed of the square
square_size = 50
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2
speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the red square
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
