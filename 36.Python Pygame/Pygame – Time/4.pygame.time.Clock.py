# importing the pygame module
import pygame

# initialising the pygame
pygame.init()

# declaring a variable i with value 0
i = 0

# creating a clock object
clock = pygame.time.Clock()

# creating a loop for 5 iterations
while i < 5:
    # setting fps of programm to max 1 per seconf
    clock.tick(1)

    # printing time used in the previous tick
    print(clock.get_time())

    # printing compute the clock framerate
    print(clock.get_fps())
    i = i + 1
