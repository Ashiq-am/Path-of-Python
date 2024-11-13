# importing pycairo
import cairo

# Defining surface area
WIDTH = 3
HEIGHT = 3
PIXEL_SCALE = 200

# creating a SVG surface
# here geek95 is file name
surface = cairo.SVGSurface('geek95.svg', WIDTH*PIXEL_SCALE,
						HEIGHT*PIXEL_SCALE)

# creating a cairo context object for SVG surface
# useing Context method
context = cairo.Context(surface)

# Scaleing Surface
context.scale(PIXEL_SCALE, PIXEL_SCALE)

# Creating Rectangle For Background
context.rectangle(0, 0, WIDTH, HEIGHT)

# Color of Rectangle For Background
context.set_source_rgb(0.3, 0.5, 1)

# Filling Color in Rectangle
context.fill()

# defining color
context.set_source_rgb(1, 0, 0)

# Font Style
context.set_font_size(0.55)

# font style
context.select_font_face(
	"Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

# Creating Rectangle
context.rectangle(0.2, 0.8, 2.6, 1)

# move to x, y percentage of surface
context.move_to(0.3, 1.5)

# Display Text
context.text_path("MARVEL")

# Filling the area
context.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)

# Filling color
context.fill()

# stroke out the color and width property
context.stroke()

# printing message when file is saved
print("File Saved")
