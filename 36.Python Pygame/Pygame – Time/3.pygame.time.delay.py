# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((500, 500))

# Creating the image surface
image = pygame.image.load('gfg_logo.png')

# puting our image surface on display surface
display.blit(image, (100, 100))

# making the script wait for 5000 seconds
pygame.time.delay(5000)

# creating a running loop
while True:

    # creating a loop to cheack events that are occuring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # updating the display
    pygame.display.flip()
