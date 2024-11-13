#import module
import arcade

#specify parameters
col_spacing = 20
row_spacing = 20
lmargin = 110
bmargin = 110

# Open the window
arcade.open_window(500, 500, "BOX")

#set the background
arcade.set_background_color(arcade.color.BABY_PINK)

# Start the render process.
arcade.start_render()

# Loop for each row
for row in range(10):

	# Loop for each column
	for col in range(10):

		# Calculate our location
		x = col * col_spacing + lmargin
		y = row * row_spacing + bmargin

		# Draw the objects
		arcade.draw_circle_filled(x+1, y+2, 10, arcade.color.BLUE)

# Finish.
arcade.finish_render()

# Keep the window up.
arcade.run()
