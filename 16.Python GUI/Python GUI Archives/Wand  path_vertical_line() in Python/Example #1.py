from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    draw.stroke_width = 2
    draw.stroke_color = Color('black')
    draw.fill_color = Color('white')
    draw.path_start()

    # Start middle-left
    draw.path_move(to=(10, 50))

    # Line to top-right
    draw.path_vertical_line(100)
    draw.path_finish()
    with Image(width=200,
               height=200,
               background=Color('lightgreen')) as image:
        draw(image)
        image.save(filename="pathvline.png")
