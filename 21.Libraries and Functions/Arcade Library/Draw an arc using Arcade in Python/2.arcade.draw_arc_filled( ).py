# import arcade module
import arcade

# Open the window. Set the window title and
# dimensions (width and height)
arcade.open_window(600, 600, "Draw an arc for GfG ")

# set a background color
arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

# function for drawing arc
arcade.draw_arc_filled(150, 144, 85, 86,
					arcade.color.BOTTLE_GREEN, 90, 360, 45, 54)

# finished drawing
arcade.finish_render()

# to diaplay everything
arcade.run()
