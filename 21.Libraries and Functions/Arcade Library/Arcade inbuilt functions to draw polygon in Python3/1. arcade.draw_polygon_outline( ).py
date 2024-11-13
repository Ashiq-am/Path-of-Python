import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Draw a polygon for GfG ")

arcade.set_background_color(arcade.color.ORANGE)

# Start the render process.
arcade.start_render()

point_list = ((30, 240),
			(45, 240),
			(60, 255),
			(60, 285),
			(45, 300),
			(30, 300))
arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)

arcade.finish_render()

arcade.run()
