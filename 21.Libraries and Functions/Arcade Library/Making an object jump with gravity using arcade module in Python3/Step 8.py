# See if we hit the bottom
if draw.y < BALL_RADIUS and draw.delta_y < 0:

		if draw.delta_y * -1 > GRAVITATIONAL_CONSTANT * 15:
			draw.delta_y *= -BOUNCE
		else:
			draw.delta_y *= -BOUNCE / 2
