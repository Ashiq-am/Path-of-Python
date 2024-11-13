# import IMage from wand.image module
from wand.image import Image

# expression string for fx()
fx_filter ="(hue > 0.9 || hue < 0.1) ? u : lightness"

with Image(filename ="koala.jpeg") as img:
    with img.fx(fx_filter) as filtered_img:
        filtered_img.save(filename ="fx-koala.jpeg")
