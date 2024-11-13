# imports Pil module
import PIL

# creating image object which is of specific color
im = PIL.Image.new(mode = "RGB", size = (200, 200),
						color = (153, 153, 255))

# this will show image in any image viewer
im.show()
