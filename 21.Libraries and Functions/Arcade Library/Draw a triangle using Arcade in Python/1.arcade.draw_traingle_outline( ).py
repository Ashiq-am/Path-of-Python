#import module
import arcade

# Open the window. Set the window title and
# dimensions (width and height)
arcade.open_window(600, 600, "Draw a triangle for GfG ")

# set background color
arcade.set_background_color(arcade.color.BLACK)

# Start the render process.
arcade.start_render()

# triangle function
arcade.draw_triangle_outline(300, 200,
							80, 80,
							100, 300,
							arcade.color.YELLOW, 1)


# finished drawing
arcade.finish_render()

# display everything
arcade.run()
