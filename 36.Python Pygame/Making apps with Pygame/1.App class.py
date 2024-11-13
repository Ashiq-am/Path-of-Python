# importing pygame and we can call it by using py
import pygame as py

# importing all the libraries of pygame.local
from pygame.locals import *


# this is a simple App class in pygame


class App_Class:

    def __init__(self):

        # initializing the function for app
        # class to declare the changeable content
        py.init()
        App_Class.screen = py.display.set_mode(
            # size of window will be 540x340
            (540, 340))
        App_Class.running = True

    def play(self):
        # this will run until the window is visible
        while App_Class.running:
            for event in py.event.get():

                # check whether the cancel
                # button is pressed or not
                if event.type == QUIT:
                    App_Class.running = False

        py.quit()


if __name__ == '__main__':
    App_Class().play()
