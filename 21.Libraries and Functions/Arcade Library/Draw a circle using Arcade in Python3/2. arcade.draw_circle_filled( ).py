#import module
import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Draw a circle for GfG ")

# set background
arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

# draw circle
arcade.draw_circle_filled(300, 450, 78, arcade.color.PINK, 0)


# finish drawing
arcade.finish_render()

# to display everything
arcade.run()
