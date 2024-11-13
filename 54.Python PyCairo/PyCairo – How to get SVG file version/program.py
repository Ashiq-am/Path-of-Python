# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:
    # creating a cairo context object
    context = cairo.Context(surface)

    # creating a rectangle(square)
    context.rectangle(100, 100, 100, 100)

    # setting color of the context
    context.set_source_rgba(0.4, 1, 0.4, 1)

    # stroke out the color and width property
    context.stroke()

    # getting all the svg versions avaialble
    versions = surface.get_versions()

# printing the versions
print("Value= " + str(versions))
