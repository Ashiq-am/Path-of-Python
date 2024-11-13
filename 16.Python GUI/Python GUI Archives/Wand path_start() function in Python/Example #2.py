from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    draw.stroke_width = 2
    draw.stroke_color = Color('black')
    draw.path_start()

    # Start middle-left
    draw.path_move(to=(100, 100))

    # draw a vertical line from path initial point
    draw.path_vertical_line(1)

    # Close first & last points
    draw.path_close()
    draw.path_finish()
    with Image(width=200,
               height=200,
               background=Color('green')) as image:
        draw(image)
        image.save(filename="pathstart.png")
