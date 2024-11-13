#import module
import arcade

# specigy spacing
Column_spacing = 20
Row_spacing = 20
Left_margin = 110
Bottom_margin = 400

# Open the window and set the background
arcade.open_window(700, 700, "BOX")

# set background color
arcade.set_background_color(arcade.color.BABY_PINK)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Loop for each row
for row in range(8):
	# Loop for each column
	for column in range(8):
		# Calculate our location
		x = column * Column_spacing + Left_margin
		y = row * Row_spacing + Bottom_margin

		# Draw the item
	arcade.draw_triangle_filled(x + 40, y,
								x, y - 100,
								x + 80, y - 100,
								arcade.color.DARK_GREEN)

arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, 300, 230,
									arcade.color.DARK_BROWN)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

# This code is contributed by pulkitagarwal03pulkit
