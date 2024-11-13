def main():
    # Open up our window
    arcade.open_window(WIDTH, HEIGHT, TITLE)
    arcade.set_background_color(arcade.color.GREEN)

    # Tell the computer to call the draw
    # command at the specified interval.
    arcade.schedule(draw, 1 / 80)

    # Run the program
    arcade.run()

    # When done running the program, close the window.
    arcade.close_window()


main()
