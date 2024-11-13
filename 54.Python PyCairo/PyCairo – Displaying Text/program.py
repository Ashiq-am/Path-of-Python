# code
import cairo

print("GFG")
# importing pycairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:
    # creating a cairo context object for SVG surface
    # using Context method
    context = cairo.Context(surface)

    # setting color of the context
    context.set_source_rgb(0, 0, 0)

    # approximate text height
    context.set_font_size(25)

    # Font Style
    context.select_font_face(
        "Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    # position for the text
    context.move_to(50, 50)

    # displays the text
    context.show_text("GeeksForGeeks")

    # stroke out the color and width property
    context.stroke()

# printing message when file is saved
print("File Saved")
