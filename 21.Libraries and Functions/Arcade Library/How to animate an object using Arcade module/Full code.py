# Import required module
import arcade


# Set up the constants

# Size of the screen
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Bouncing Box"

# Size of the rectangle
RECT_WIDTH = 50
RECT_HEIGHT = 50


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


# Set initial positions
on_draw.center_x = 100
on_draw.center_y = 50
on_draw.delta_x = 115
on_draw.delta_y = 130


# Driver code

# Open up our window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)

# Tell the computer to call the draw command at the specified interval.
arcade.schedule(on_draw, 1 / 80)

# Run the program
arcade.run()
