# Importing arcade module
import arcade


# Creating MainGame class
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, title="Keyboard Inputs")

    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()

    # Creating function to check button is pressed
    # or not
    def on_key_press(self, symbol, modifier):

        # Checking the button pressed
        # is up arrow key or not
        if symbol == arcade.key.UP:
            print("Upper arrow key is pressed")

    # Creating function to check button is released
    # or not
    def on_key_release(self, symbol, modifier):

        # Checking the button pressed
        # is up arrow key or not
        if symbol == arcade.key.UP:
            print("Upper arrow key is released")


# Calling MainGame class
MainGame()
arcade.run()
