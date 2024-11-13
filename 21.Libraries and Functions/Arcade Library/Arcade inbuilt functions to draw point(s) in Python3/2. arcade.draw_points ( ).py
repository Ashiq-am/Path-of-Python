import arcade

# Open the window
arcade.open_window(600, 600, "Draw a point for GfG ")

arcade.set_background_color(arcade.color.ORANGE)

# Start the render process.
arcade.start_render()

# Draw a points
point_list = ((165, 495),
			(165, 480),
			(165, 465),
			(195, 495),
			(195, 480),
			(195, 465))
arcade.draw_points(point_list, arcade.color.GREEN , 10)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
