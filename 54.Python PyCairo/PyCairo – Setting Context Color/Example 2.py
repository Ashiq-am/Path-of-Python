# importing pycairo
import cairo

# creating a SVG surface
# here geek007 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek007.svg", 700, 700) as surface:
    # creating a cairo context object for SVG surface
    # useing Context method
    context = cairo.Context(surface)

    # setting color of the context
    context.set_source_rgba(4, 0, 4, 0.5)

    # setting of line width
    context.set_line_width(40)

    # move the context to x,y position
    context.move_to(40, 30)

    # creating a rectangle(square)
    context.rectangle(100, 100, 100, 100)

    # stroke out the color and width property
    context.stroke()

# printing message when file is saved
print("File Saved")
