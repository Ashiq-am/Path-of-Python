# Import required modules
import arcade

# Specify Parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to GeeksForGeeks "

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BABY_BLUE)

# Start drawing
arcade.start_render()

# Draw ellipse
arcade.draw_ellipse_outline(
	400, 363, 250, 130, arcade.color.AMBER, 10, 180, -1)

# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()
