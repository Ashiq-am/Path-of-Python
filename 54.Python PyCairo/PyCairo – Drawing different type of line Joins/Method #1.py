# importing pycairo
import cairo

# creating a SVG surface
# here geek94 is file name
# & 700, 700 is dimension
with cairo.SVGSurface("geek94.svg", 700, 700) as surface:
    # creating a cairo context object
    # for SVG surface
    # useing Context method
    context = cairo.Context(surface)
    context.set_source_rgba(0, 0, 0, 1)
    context.set_line_width(14)

    context.rectangle(30, 30, 100, 100)

    # Setting line join style
    context.set_line_join(cairo.LINE_JOIN_MITER)

    # stroke out the color and width property
    context.stroke()

    # printing message when file is saved
    print("File Saved")
