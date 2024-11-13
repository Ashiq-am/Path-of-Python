def draw(_delta_time):

	# Start the render.
	arcade.start_render()

	# Draw ball
	arcade.draw_circle_filled(draw.x, draw.y, BALL_RADIUS,
							arcade.color.RED)

	draw.x += draw.delta_x
	draw.y += draw.delta_y
	draw.delta_y -= GRAVITATIONAL_CONSTANT
