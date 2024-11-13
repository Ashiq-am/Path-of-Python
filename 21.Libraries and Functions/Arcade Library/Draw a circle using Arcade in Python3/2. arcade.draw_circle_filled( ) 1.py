#import module
import arcade

# Open the window. Set the window title and
# dimensions (width and height)
arcade.open_window(600, 600, "Draw a circle for GfG ")

# set background
arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

# snowman upper part
arcade.draw_circle_filled(300, 450, 68, arcade.color.SKY_BLUE, 0)

# snowman eyes
arcade.draw_circle_filled(289, 475, 8, arcade.color.BLACK, 0)
arcade.draw_circle_filled(329, 475, 8, arcade.color.BLACK, 0)

# snowman lower part
arcade.draw_circle_filled(300, 350, 88, arcade.color.BLUE, 0)
arcade.draw_circle_filled(300, 250, 108, arcade.color.SKY_BLUE, 0)

# finish drawing
arcade.finish_render()

# to display everything
arcade.run()
