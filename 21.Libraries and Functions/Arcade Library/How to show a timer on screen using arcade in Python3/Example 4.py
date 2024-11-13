def on_draw(self):

	# Start the render.
	arcade.start_render()

	# Calculate minutes
	minutes = int(self.total_time) // 60

	# Calculate seconds by using a modulus
	seconds = int(self.total_time) % 60

	# Figure out your output
	output = f"Time: {minutes:02d}:{seconds:02d}"

	# Output the timer text.
	arcade.draw_text(output, 300, 300, arcade.color.BOTTLE_GREEN, 45)
