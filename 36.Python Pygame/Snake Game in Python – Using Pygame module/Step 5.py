# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the
    # program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()
