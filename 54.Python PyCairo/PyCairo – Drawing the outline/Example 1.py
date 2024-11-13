# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name &
# 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:
    # creating a cairo context
    # object for SVG surface
    # using Context method
    context = cairo.Context(surface)

    # Creating shape
    context.rectangle(25, 50, 50, 120)

    # setting color of the context
    context.set_source_rgb(1, 0, 0)

    # Fill the color inside
    context.fill()

    # Creating shape
    context.rectangle(125, 50, 50, 120)

    # setting color of the context
    context.set_source_rgb(0, 1, 1)

    # Setting outline width
    context.set_line_width(4)

    # stroke out the color and width property
    context.stroke()

    # Creating shape
    context.rectangle(225, 50, 50, 120)

    # setting color of the context for inside
    context.set_source_rgb(0, 0, 1)

    # Preserving inside color of object
    context.fill_preserve()

    # setting color of the context for outline
    context.set_source_rgb(1, 1, 0)

    context.set_line_width(4)

    # stroke out the color and width property
    context.stroke()

# printing message when file is saved
print("File Saved")
