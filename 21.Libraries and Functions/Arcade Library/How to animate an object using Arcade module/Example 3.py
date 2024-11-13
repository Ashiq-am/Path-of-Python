# Explicilt function generate animated bouncing box
def on_draw(delta_time):

	# Start the render.
	arcade.start_render()

	arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,
								RECT_WIDTH, RECT_HEIGHT,
								arcade.color.GREEN)

	on_draw.center_x += on_draw.delta_x * delta_time
	on_draw.center_y += on_draw.delta_y * delta_time

	# Figure out if we hit the edge and need to reverse.
	if on_draw.center_x < RECT_WIDTH // 2 \
			or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
		on_draw.delta_x *= -1
	if on_draw.center_y < RECT_HEIGHT // 2 \
			or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
		on_draw.delta_y *= -1
