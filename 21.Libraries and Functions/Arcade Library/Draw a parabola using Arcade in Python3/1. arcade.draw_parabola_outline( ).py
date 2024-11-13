# import module
import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Draw a parabola for GfG ")

# set background
arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

# function to draw a parabola
arcade.draw_parabola_outline(50, 80, 100, 120, arcade.color.GREEN, 10, 0)

# finish drawing
arcade.finish_render()
