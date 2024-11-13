import arcade

# Open the window. Set the window title and
# dimensions (width and height)
arcade.open_window(600, 600, "Draw an arc for GfG ")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

arcade.draw_arc_outline(150, 81, 15, 36,
						arcade.color.BLACK, 90, 360)

arcade.finish_render()

arcade.run()
