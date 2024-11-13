# import IMage from wand.image module
from wand.image import Image

# expression string for fx()
fx_filter ="(luma > 0.9 || luma < 0.1) ? u : lightness"

with Image(filename ="koala.jpeg") as img:
    with img.fx(fx_filter) as filtered_img:
        filtered_img.save(filename ="fx-koala.jpeg")
