# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

# creating a running loop
while True:

    # creating a loop to cheack events that
    # are occuring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checking if keydown event happend or not
        if event.type == pygame.KEYDOWN:
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")
