# importing pycairo
import cairo
import math


# Creating function for make roundrect shape
def roundrect(context, x, y, width, height, r):
    context.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)

    context.arc(x + width - r, y + r, r, 3 * math.pi / 2, 0)

    context.arc(x + width - r, y + height - r, r, 0, math.pi / 2)

    context.arc(x + r, y + height - r, r, math.pi / 2, math.pi)

    context.close_path()


# creating a SVG surface
# here geek95 is file name &
# 700, 700 is dimension


with cairo.SVGSurface("geek95.svg", 700, 700) as surface:
    # creating a cairo context object for SVG surface
    # useing Context method
    context = cairo.Context(surface)

    # setting width of the context
    context.set_line_width(10)

    # setting color of the context
    context.set_source_rgb(0, 0, 0.5)

    # Call the function
    roundrect(context, 100, 100, 400, 200, 50)

    # stroke out the color and width property
    context.stroke()

# printing message when file is saved
print("File Saved")
