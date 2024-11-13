import arcade


def draw_tree(x, y):

	# Draw the triangle on top of the trunk
	arcade.draw_triangle_filled(x + 40, y,
								x, y - 100,
								x + 80, y - 100,
								arcade.color.DARK_GREEN)

	# Draw the trunk
	arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
									arcade.color.DARK_BROWN)


def main():

	# Open the window
	arcade.open_window(600, 600, "TREE")
	arcade.set_background_color(arcade.color.SKY_BLUE)

	# Start the render process.
	arcade.start_render()

	# Call our drawing functions.
	draw_tree(50, 250)

	# Finish the render.
	arcade.finish_render()

	# Keep the window up.
	arcade.run()


main()
