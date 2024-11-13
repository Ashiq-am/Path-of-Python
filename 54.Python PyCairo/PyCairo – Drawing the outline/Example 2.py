# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:
    # creating a cairo context
    # object for SVG surface
    # using Context method
    context = cairo.Context(surface)

    # Creating shape
    context.arc(500, 60, 40, 0, 2 * 22 / 7)

    # setting color of the context for inside
    context.set_source_rgb(0, 0, 0)

    # Preserving inside color of object
    context.fill_preserve()

    # setting color of the context for outline
    context.set_source_rgb(1, 1, 0)

    # Setting outline width
    context.set_line_width(4)

    # stroke out the color and width property
    context.stroke()


# printing message when file is saved
print("File Saved")
