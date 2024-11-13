import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Draw a point for GfG ")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

# Draw a point
arcade.draw_point(60, 495, arcade.color.RED, 10)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
