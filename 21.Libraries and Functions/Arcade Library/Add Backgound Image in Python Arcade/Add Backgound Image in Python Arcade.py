# Importing arcade module
import arcade


# Creating MainGame class
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, title="Background Image")

        # Loading the background image
        self.background = arcade.load_texture("BACKGROUND.png")

    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()

        # Drawing the background image
        arcade.draw_texture_rectangle(300, 300, 600,
                                      600, self.background)


# Calling MainGame class
MainGame()
arcade.run()
