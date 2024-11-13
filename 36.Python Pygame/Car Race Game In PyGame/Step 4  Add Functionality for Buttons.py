# Function to create a button with specified parameters
# msg: The text to be displayed on the button
# x, y: The coordinates of the top-left corner of the button
# w, h: The width and height of the button
# ic: The color of the button when inactive
# ac: The color of the button when active (hovered over)
# action: The action to be performed when the button is clicked

def button(msg, x, y, w, h, ic, ac, action=None):
    # Get the current mouse position
    mouse = pygame.mouse.get_pos()
    # Get the current state of mouse buttons
    click = pygame.mouse.get_pressed()

    # Check if mouse is within the button's boundaries
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        # Draw button with active color
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))

        # Check if left mouse button is clicked
        # and action is specified
        if click[0] == 1 and action != None:
            # If action is "play", call the countdown()
            if action == "play":
                countdown()
            # If action is "quit", quit the game
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()

            elif action == "intro":
                introduction()

            # If action is "menu", call the intro_loop() function
            elif action == "menu":
                intro_loop()
             # If action is "pause", call the paused() function
            elif action == "pause":
                paused()
                # If action is "unpause", call the unpaused() function
                unpaused()

            elif action == "unpause":


    else:
        # Draw button with inactive color
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_objects(msg, smalltext)
        textrect.center = ((x+(w/2)), (y+(h/2)))
        gamedisplays.blit(textsurf, textrect)
