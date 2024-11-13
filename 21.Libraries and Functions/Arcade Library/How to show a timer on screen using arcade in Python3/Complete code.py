#import module
import arcade

# screen parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Timer "

# define class


class MyTimer(arcade.Window):

	def setup(self):
		arcade.set_background_color(arcade.color.WHITE)
		self.total_time = 0.0

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

	# update
	def on_update(self, delta_time):
		self.total_time += delta_time

# main function
def main():
	window = MyTimer()
	window.setup()
	arcade.run()


# call main function
main()
