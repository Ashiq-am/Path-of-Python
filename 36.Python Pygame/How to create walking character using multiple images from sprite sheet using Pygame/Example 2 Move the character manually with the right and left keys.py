import pygame as py
import os

py.init()

# THE WIDTH AND HEIGHT OF OUR SCREEN
win = py.display.set_mode((600, 480))

py.display.set_caption("Sprite pygame direction movement")

# DECLARING THE LOCATION OF THE FOLDER
# IN WHICH ALL THE LEFT
# AND RIGHT IMAGES FOR THE MOVEMENT
folderPath_left = "Character_images_left"
folderPath_right = "Character_images_right"

# STORE THE FOLDER LOCATION IN ONE LIST
myList_right = os.listdir(folderPath_right)
myList_left = os.listdir(folderPath_left)

# PICTURE FOR RIGHT MOVEMENT
movement_right = []
for imPath in myList_right:
    # APPENDING THE IMAGES WITH THE
    # LOCATION IN A LIST
    movement_right.append(py.image.load(f'{folderPath_right}/{imPath}'))

# PICTURE FOR LEFT MOVEMENT
movement_left = []
for imPath in myList_left:
    # APPENDING THE IMAGES WITH THE
    # LOCATION IN A LIST
    movement_left.append(py.image.load(f'{folderPath_left}/{imPath}'))

# SETTING BACKGROUND IMAGE
bg = py.image.load('hacker.gif')

# SETTING CHARACTER IMAGE FOR THE
# STANDING POSITION
standing_position = py.image.load('r1.png')

x = 20
y = 100
width = 40
height = 100
velocity = 5

clock = py.time.Clock()

left = False
right = False
movement_count = 0


# Declaring the sprite window
def Sprite_Window():
    # To store the movement count
    global movement_count

    win.blit(bg, (1, 1))
    if movement_count + 1 >= 20:
        movement_count = 0

    # To move the character right side of
    # the sprite window
    if right:
        win.blit(movement_right[movement_count // 4], (x, y))
        movement_count = movement_count + 1

    # To move the character left side of
    # the sprite window
    elif left:
        win.blit(movement_left[movement_count // 4], (x, y))
        movement_count = movement_count + 1

    # If user will not press any keys then
    # the image in the sprite
    # window will be in the standing position
    else:
        win.blit(standing_position, (x, y))
        movement_count = 0

    # To update the display screen
    py.display.update()


# This will be used to quit the window
run = 1
while run:

    # This will manage the frame rate and provide
    # more smoothness to the movement
    clock.tick(33)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = 0
    keys = py.key.get_pressed()

    # To move to the end of the screen
    if keys[py.K_RIGHT] and x < 480 - velocity - width:

        # For moving in the right direction
        x += velocity
        right = True
        left = False

    # To move to the end of the screen
    elif keys[py.K_LEFT] and x > velocity - width:

        # For moving in the left direction
        x -= velocity
        right = False
        left = True
    else:
        left = False
        right = False
        movement_count = 0

    Sprite_Window()
py.quit()
