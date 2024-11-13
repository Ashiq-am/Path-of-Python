# importing pycairo
import cairo

# getting all the svg versions avaialble
import surface as surface

versions = surface.get_versions()

# Selecting version from list
version = versions[1]

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:

	# Restriction to version
	surface.restrict_to_version(version)

	# creating a cairo context object
	context = cairo.Context(surface)

	# creating a rectangle(square)
	context.rectangle(10, 10, 100, 100)

	# setting color of the context
	context.set_source_rgba(0.4, 1, 0.4, 1)

	# stroke out the color and width property
	context.fill()

# printing
print("SVG version")
