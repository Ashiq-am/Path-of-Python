# Figure out if we hit the left or
# right edge and need to reverse.
if draw.x < BALL_RADIUS and draw.delta_x < 0:
	draw.delta_x *= -BOUNCE
elif draw.x > WIDTH - BALL_RADIUS and draw.delta_x > 0:
	draw.delta_x *= -BOUNCE
