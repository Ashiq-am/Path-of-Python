import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Draw a polygon for GfG ")

arcade.set_background_color(arcade.color.ORANGE)

# Start the render process.
arcade.start_render()

point_list = ((150, 240),
			(165, 240),
			(180, 255),
			(180, 285),
			(165, 300),
			(150, 300))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

arcade.finish_render()

arcade.run()
