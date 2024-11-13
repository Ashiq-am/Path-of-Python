# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:
    # creating a cairo context object for SVG surface
    # useing Context method
    Context = cairo.Context(surface)

    # setting color of the context
    Context.set_source_rgb(1, 0, 0)

    # approximate text height
    Context.set_font_size(50)

    # Font Style
    Context.select_font_face(
        "Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    # position for the text
    Context.move_to(35, 45)

    # displays the text
    Context.text_path("GeeksforGeeks.org")

    # Width of outline
    Context.set_line_width(2)

    # stroke out the color and width property
    Context.stroke()

# printing message when file is saved
print("File Saved")
